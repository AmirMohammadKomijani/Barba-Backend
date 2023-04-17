from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Barber,Rate
from Auth.models import User
from Auth.serializer import UserSerializer
from .serializers import BarberSerializer,BarberProfileSerializer,RateSerializer
from .filters import BarberRateFilter
from rest_framework.permissions import IsAuthenticated




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
        


# class BarberBaseProfileView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
#     def me(self, request):
#         (user, created) = User.objects.get_or_create(
#             id=request.user.id)
#         # baseInfo = User.objects.prefetch_related('user_set').all()
#         if request.method == 'GET':
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = UserSerializer(user, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)



# class BarberBaseProfileView(APIView):
#     def get(self,request):
#         queryset = User.objects.get(pk=request.user.id)
#         serializer = UserSerializer(queryset)
#         return Response(serializer.data)

#     def put(self,request):
#         user = User.objects.get(pk=request.user.id)
#         serializer = UserSerializer(user,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# class BarberBaseProfileView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # lookup_fields = ['email', 'username']
        

# class BarberBaseProfileView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return User.objects.prefetch_related('barber').all()







# class BarberBaseProfileView(ModelViewSet):
#     queryset = User.objects.prefetch_related('barber').all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
#     def me(self, request):
#         (barber, created) = User.objects.get(
#             barber=request.user.id)
#         # baseInfo = User.objects.prefetch_related('barber_set').all()
#         if request.method == 'GET':
#             serializer = UserSerializer(barber)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = UserSerializer(barber, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)















# class BarberShopImagesView(ModelViewSet):
#     serializer_class = BarberShopImagesSerializer

#     def get_serializer_context(self):
#         return {'barbershop_id':self.kwargs['barbershop_pk']}

#     def get_queryset(self):
#         return BarberShopImages.objects.filter(barbershop_id=self.kwargs['barbershop_pk'])



# class BarberView(ModelViewSet):
#     queryset = Barber.objects.all()
#     serializer_class = BarberSerializer


class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
