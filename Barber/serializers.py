from rest_framework import serializers
from .models import Barber,BarberShopImages,Rate


class BarberShopImagesSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        barbershop_id = self.context['barbershop_id']
        return BarberShopImages.objects.create(barbershop_id=barbershop_id,**validated_data)
    
    class Meta:
        model = BarberShopImages
        fields = ['background','logo']


class BarberSerializer(serializers.ModelSerializer):
    images = BarberShopImagesSerializer(many=True,read_only=True)
    class Meta:
        model = Barber
        fields = ['BarberShop','Owner','phone_Number','address',"rate",'images']



class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']
    
    

