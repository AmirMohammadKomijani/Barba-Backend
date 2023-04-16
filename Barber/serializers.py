from rest_framework import serializers
from .models import Barber,Rate


# class BarberShopImagesSerializer(serializers.ModelSerializer):
    
#     def create(self, validated_data):
#         barbershop_id = self.context['barbershop_id']
#         return BarberShopImages.objects.create(barbershop_id=barbershop_id,**validated_data)
    
#     class Meta:
#         model = BarberShopImages
#         fields = ['background','logo']


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ['id','BarberShop','Owner','phone_Number','area','address','rate','background','logo']


class BarberProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Barber
        fields = ['user_id','BarberShop','Owner','Parvaneh','phone_Number','area','address','background','logo']



class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']



