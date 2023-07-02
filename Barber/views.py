from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import generics , status
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Barber,OrderServices,Category,CategoryService,BarberDescription, Comment , BarberPremium, Rating
from .serializers import BarberInfoSerializer,BarberProfileSerializer ,BarberAreasSerializer,OrderServiceSerializer, \
                        CategorySerializer,BarberDescriptionSerializer,CategoryServiceSerializer,Get_CustomerBasketSerializer, \
                        Put_CustomerBasketSerializer,Put_BarberPanelSerializer,Get_BarberPanelSerializer,\
                        CommentSerializerOnPOST, CommentSerializerOnPUT, CommentSerializerOnGET,GetBarberPremiumSerializer,PutBarberPremiumSerializer,\
                        RatingSerializer
from .filters import BarberRateFilter,BarberPanelFilter
from rest_framework.permissions import IsAuthenticated
from Customer.models import Customer
import datetime





#######################################################
### Barber Panel Serializers

## 1/ adding category and service

class addCategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_context(self):
        return {'barber_id':self.request.user.id}

    def get_queryset(self):
        (barber,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        return Category.objects.filter(barber_id = barber)


class addCategoryServiceView(ModelViewSet):
    serializer_class = CategoryServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'category_id':self.kwargs['category_pk']}

    def get_queryset(self):
        (category,created) = Category.objects.get_or_create(id=self.kwargs['category_pk'])
        return CategoryService.objects.filter(category_id = category)


## 2/ profile and description of barbershop

class BarberProfileView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberProfileSerializer

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (barber, created) = Barber.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = BarberProfileSerializer(barber)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BarberProfileSerializer(barber, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        

class BarberDescriptionView(ModelViewSet):
    serializer_class = BarberDescriptionSerializer

    def get_queryset(self):
        barber = Barber.objects.get(user_id = self.request.user.id)
        return BarberDescription.objects.filter(barber_id = barber)
    def get_serializer_context(self):
        return {'barber_id':self.request.user.id}


## 3/ Barber management segment
from django.http import Http404

class BarberPanelView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BarberPanelFilter
    ordering_fields = ['date','time']

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return Put_BarberPanelSerializer
        return Get_BarberPanelSerializer
    
    def get_queryset(self):
        barber = Barber.objects.get(user_id = self.request.user.id)
        premium = BarberPremium.objects.select_related('barber').filter(expire_date__gt=datetime.date.today()).exists()
        if premium:
            return OrderServices.objects.filter(barber = barber)
            
        
class BarberPremiumView(APIView):
    def get(self,request):
        barber = Barber.objects.get(user_id=request.user.id)
        queryset = BarberPremium.objects.filter(barber = barber)
        serializer = GetBarberPremiumSerializer(queryset,many=True)
        return Response(serializer.data)
    

    # def put(self,request,id):
    #     (barber,created) = Barber.objects.get_or_create(user_id=request.user.id)
    #     queryset = BarberPremium.objects.filter(barber = barber)
    #     serializer = PutBarberPremiumSerializer(queryset,data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data)


class BarberBuyPremiumView(ModelViewSet):
    serializer_class = PutBarberPremiumSerializer

    def get_queryset(self):
        (barber,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        # (premium,create) = BarberPremium.objects.get_or_create(barber = barber)
        return BarberPremium.objects.filter(barber = barber)
 

#######################################################
### customer ordering and paying process
## 1/ Barber info

class BarberInfoView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberInfoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']
    
    @action(methods=["POST"], permission_classes=[IsAuthenticated], detail=True)
    def rate(self, request,pk=None, *args, **kwargs):
        # Get all ratings for the specified barber and customer
        customer = request.user.customer
        barber = get_object_or_404(Barber, pk=pk)
        ratings = Rating.objects.filter(barber=barber, customer=customer)
        if ratings.exists():
            # If there are multiple ratings, delete all but the most recent one
            if ratings.count() > 1:
                old_ratings = ratings.order_by('-created_at')[:len(ratings)-1]
                # old_ratings.delete()
                for old_rating in old_ratings:
                    old_rating.delete()
            # Update the most recent rating with the new rating value
            rating =ratings.order_by('-created_at').first()
            serializer =RatingSerializer(rating, data=request.data)
        else :
                # If there are no ratings, create a new rating            
                serializer = RatingSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(customer=customer, barber=barber)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Save the updated rating
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        


## 2/ Ordering a service

class OrderServiceView(ModelViewSet):
    serializer_class = OrderServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        return OrderServices.objects.filter(customer_id = customer)

## 3/ Customer Basket

class CustomerBasketView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return Put_CustomerBasketSerializer
        return Get_CustomerBasketSerializer
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        # history = OrderServices.objects.filter(customer_id = customer)
        return OrderServices.objects.filter(customer = customer,date__gt =  datetime.date.today(),status = "ordering")


class CustomerOrderHistoryView(ModelViewSet):
    serializer_class = Get_CustomerBasketSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date','status']
    # filterset_class = CustomerOrderHistoryFilter
    ordering_fields = ['date','time']
    
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        return OrderServices.objects.filter(customer_id = customer)


###############################################################
### extra information    

class Areas(ModelViewSet):
    serializer_class = BarberAreasSerializer
    pagination_class=None

    def get_queryset(self):
        return Barber.objects.values('area').distinct()



# class CommentCreateView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated,]

#     def perform_create(self, serializer):
#         serializer.save(customer=self.request.user.customer)
# class CommentReplyView(UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated,]

#     def perform_update(self, serializer):
#         if self.request.useer.barber:
#             serializer.save(barber=self.request.user.barber)
#         return Response("google.com",status=404 )
        
class CommentCreateAPIView(CreateAPIView):#, generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializerOnPOST
    queryset = Comment.objects.all()    
    
    def get_serializer_context(self):
        return {"customer_id":self.request.user.id}
    # def update(self, request, *args, **kwargs):
    #     # serializer_class = 
    #     return super().update(request, *args, **kwargs)
class CommentReplyAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializerOnPUT
    queryset = Comment.objects.all()    
    # def perform_create(self, serializer):
    #     # if self.request.user.barber == comment.barber:
    #     # if self.request.user.barber == self.context['request'].user.barber:
    #         comment_id = self.kwargs.get('comment_id')
    #         comment = get_object_or_404(Comment, id=comment_id)
    #         serializer.save(barber=self.request.user.barber, comment=comment)
        # serializer.save(comment=comment)
class  CommentShowAPIView(generics.ListAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializerOnGET
    def get_queryset(self):
        (barber_id,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        return Comment.objects.filter(barber_id=barber_id)