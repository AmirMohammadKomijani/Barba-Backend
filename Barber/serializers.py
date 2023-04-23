from rest_framework import serializers
from .models import Barber,Rate,Service
from Auth.serializer import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = Service
        fields = ['service','price','service_pic','category']

class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = Service
        fields = ['service','price','service_pic','category']

    
    def save(self, **kwargs):
        barber, created = Barber.objects.get_or_create(user_id=self.context['user_id'])
        self.validated_data.update({'barber': barber, **kwargs})
        service = Service.objects.create(**self.validated_data)
        return service
    
    # def create(self,validated_data):
    #     services = Service.objects.create(**validated_data)
    #     return services
    
    # def update(self, instance, validated_data):
    #     instance.service = validated_data.get('service',instance.service)
    #     instance.price = validated_data.get('price',instance.price)
    #     instance.service_pic = validated_data.get('service_pic',instance.service_pic)
    #     instance.category = validated_data.get('category',instance.category)

    #     instance.save()
    #     return instance
        
        
# class CategorySerializer(serializers.ModelSerializer):
#     services = ServiceSerializer()
#     class Meta():
#         model = Category
#         fields = ['category','barber','services']
    
    # def create(self, validated_data):
    #     services_data = validated_data.pop('services', [])
    #     category = Category.objects.create(**validated_data)
    #     for service_data in services_data:
    #         Service.objects.create(catg=category, **service_data)
    #     return category
    
    # def update(self, instance, validated_data):
    #     instance.category = validated_data.get('category',instance.category)
    #     instance.barber = validated_data.get('barber',instance.barber)

    #     service_data = validated_data.pop('services', None)
    #     if service_data:
    #         service = instance.service
    #         service_serializer = ServiceSerializer(service, data=service_data)
    #         service_serializer.is_valid(raise_exception=True)
    #         service_serializer.save()

    #     instance.save()
    #     return instance





class BarberSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    class Meta:
        model = Barber
        fields = ['id','BarberShop','Owner','phone_Number','area','address','rate','background','logo','services']


class BarberProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta():
        model = Barber
        fields = ['BarberShop','Owner','Parvaneh','phone_Number','area','address','background','logo','user',]


    def update(self, instance, validated_data):
        instance.BarberShop = validated_data.get('BarberShop',instance.BarberShop)
        instance.Owner = validated_data.get('Owner',instance.Owner)
        instance.Parvaneh = validated_data.get('Parvaneh',instance.Parvaneh)
        instance.phone_Number = validated_data.get('phone_Number',instance.phone_Number)
        instance.area = validated_data.get('area',instance.area)
        instance.address = validated_data.get('address',instance.address)
        instance.background = validated_data.get('background',instance.background)
        instance.logo = validated_data.get('logo',instance.logo)
        instance.save()
        
        user_data = validated_data.pop('user', None)
        user = instance.user
        user_serializer = UserSerializer(user, data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return instance


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']




    



