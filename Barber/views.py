from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet,ViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Barber,Rate,OrderServices,Category,CategoryService,TotalPrice
from .serializers import BarberSerializer,BarberProfileSerializer,RateSerializer,BarberAreasSerializer,OrderServiceSerializer,CategorySerializer,CategoryServiceSerializer,Get_CustomerBasketSerializer,Put_CustomerBasketSerializer,Put_BarberPanelSerializer,Get_BarberPanelSerializer
from .filters import BarberRateFilter,BarberPanelPriceFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Auth.models import User
from Customer.models import Customer
import datetime



# class OrderServiceView(ModelViewSet):
#     queryset = OrderServices.objects.all()
#     serializer_class = OrderServiceSerializer
#     permission_classes = [IsAuthenticated]

#     # def get_queryset(self):
#     #     return OrderServices.objects.filter(service_id = self.kwargs['pk'])

#     def get_serializer_context(self):
#         return {'user_id':self.request.user.id,'barber_id':self.kwargs['info_pk'],'service_id':self.kwargs['pk']}


# class CustomerBuyWalletView(ModelViewSet):
#     # queryset = Customer.objects.all()
#     serializer_class = CustomerBuyWalletSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Customer.objects.filter(user_id = self.request.user.id)


# class TotalPriceView(ModelViewSet):
#     serializer_class = TotalPriceSerializer

#     def get_queryset(self):
#         (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
#         return TotalPrice.objects.filter(customer_id = customer)

class BarberPanelView(ModelViewSet):
    #queryset = OrderServices.objects.all()
    # serializer_class = Get_BarberPanelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status','date']
    # filterset_class = BarberPanelPriceFilter
    ordering_fields = ['date','time']

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return Put_BarberPanelSerializer
        return Get_BarberPanelSerializer
    

    def get_queryset(self):
        (barber,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        return OrderServices.objects.filter(barber_id = barber)#.filter(date = datetime.date.today())


class CustomerBasketView(ModelViewSet):
    #queryset = OrderServices.objects.all()
    # serializer_class = Get_CustomerBasketSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return Put_CustomerBasketSerializer
        return Get_CustomerBasketSerializer
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        return OrderServices.objects.filter(customer_id = customer)

# class CustomerBasketTotalPriceView(ModelViewSet):
#     # queryset = OrderServices.objects.all()
#     serializer_class = CustomerBasketTotalPriceSerializer

#     def get_queryset(self):
#         (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
#         return OrderServices.objects.filter(customer_id = customer) 

class addCategoryView(ModelViewSet):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_context(self):
        return {'barber_id':self.request.user.id}

    def get_queryset(self):
        (barber,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        return Category.objects.filter(barber_id = barber)


class addCategoryServiceView(ModelViewSet):
    # queryset = CategoryService.objects.all()
    serializer_class = CategoryServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'category_id':self.kwargs['category_pk']}

    def get_queryset(self):
        (category,created) = Category.objects.get_or_create(id=self.kwargs['category_pk'])
        return CategoryService.objects.filter(category_id = category)


class OrderServiceView(ModelViewSet):
    # queryset = OrderServices.objects.all()
    serializer_class = OrderServiceSerializer
    permission_classes = [IsAuthenticated]


    # def create(self, request, *args, **kwargs):
    #     serializer = OrderServiceSerializer(data=request.data,
    #         context={'user_id':self.request.user.id})
    #     serializer.is_valid(raise_exception=True)
    #     order = serializer.save()
    #     serializer = OrderServiceSerializer(order)
    #     return Response(serializer.data)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        return OrderServices.objects.filter(customer_id = customer)



# class addService(ModelViewSet):
#     # queryset = Service.objects.all()
#     # serializer_class = ServiceSerializer
#     permission_classes = [IsAuthenticated]
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return CreateServiceSerializer
#         return ServiceSerializer

#     def get_queryset(self):
#         (barber,created) = Barber.objects.only('id').get_or_create(user_id = self.request.user.id)
#         return Service.objects.filter(barber_id = barber).all()
    
#     def get_serializer_context(self):
#         return {'user_id':self.request.user.id}




class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']
    # permission_classes = [IsAuthenticated]


class BarberProfileView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberProfileSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (barber, created) = Barber.objects.get_or_create(
            user_id=request.user.id)
        # baseInfo = User.objects.prefetch_related('barber_set').all()
        if request.method == 'GET':
            serializer = BarberProfileSerializer(barber)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BarberProfileSerializer(barber, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class Areas(ModelViewSet):
    serializer_class = BarberAreasSerializer
    pagination_class=None

    def get_queryset(self):
        return Barber.objects.values('area').distinct()
        

        
class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer



