from rest_framework import serializers
from .models import Customer



class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','phone_Number','area','profile_pic']
