from django.shortcuts import render
from django.views import View
from rest_framework.generics import RetrieveUpdateAPIView 
from .models import CustomerProfile
from Auth.models import Customer
from .serializers import CustomerProfileSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.

class CustomerProfileView(RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer
