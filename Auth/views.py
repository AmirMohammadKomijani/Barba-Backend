from rest_framework import generics
from .models import Customer,Barber
from .serializer import BarberCreateSerializer,CustomerCreateSerializer,CustomerTokenObtainPairSerializer,BarberTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView



class CustomerRegisterView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer
    permission_classes = (AllowAny,)

class BarberRegisterView(generics.CreateAPIView):
    queryset = Barber.objects.all()
    serializer_class = BarberCreateSerializer
    permission_classes = (AllowAny,)


class CustomerLoginView(TokenObtainPairView):
    serializer_class = CustomerTokenObtainPairSerializer


class BaberLoginView(TokenObtainPairView):
    serializer_class = BarberTokenObtainPairSerializer

