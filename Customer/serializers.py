from rest_framework import serializers
from .models import CustomerProfile
from Auth.models import Customer

from django.contrib.auth.models import User

# # class CustomerProfileSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomerProfile
# #         fields = ['first_name','last_name','phone_Number','email']


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", 'first_name','last_name','phone_Number','email', "profile_picture"]

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

# class CustomerProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Customer
#         fields = ['id', 'user', 'bio', 'avatar']

#     def update(self, instance, validated_data):
#         user_data = validated_data.pop('user')
#         user_serializer = UserSerializer(instance.user, data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#         return super().update(instance, validated_data)