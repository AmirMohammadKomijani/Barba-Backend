from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView 
from .models import Customer
from .serializers import CustomerProfileSerializer,Customers,CustomerWalletSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from decimal import Decimal

# Create your views here.

class CustomerProfileView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customers
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerProfileSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerProfileSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @action(detail=False, methods=['GET','PUT'], permission_classes=[IsAuthenticated],url_path="add_credits", url_name="add_credits")
    def add_credits(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        
        if request.method == 'GET':
            serializer = CustomerWalletSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            credit = Decimal(request.data['credit'])
            if credit < 0:
                return Response({"error": "Credit cannot be negative"}) 
            customer= Customer.objects.get(user_id=request.user.id)            
            customer.credit += credit
            serializer = CustomerWalletSerializer(customer,data=request.data)
            serializer.is_valid(raise_exception=True)
            customer.save()
            return Response(serializer.data) 

