from rest_framework import serializers
from .models import Barber,Rate
from Auth.serializer import UserSerializer



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


    # def update(self,instance , validated_data):
        
    #     categories_data = validated_data.pop('categories')
    #     categories = instance.categories
    #     cate = []
    #     for data in categories_data:
    #         cate.append(models.Category.objects.get(name=data["name"]))
    #     categories.set(cate)

    #     instance.title = validated_data.get('title' , instance.title)
    #     instance.room_type = validated_data.get("room_type" , instance.room_type)
    #     instance.link = validated_data.get('link' , instance.link)
    #     instance.password = validated_data.get('password' , instance.password)
    #     instance.description = validated_data.get('description' , instance.description)
    #     instance.start_date = validated_data.get('start_date' , instance.start_date)
    #     instance.end_date = validated_data.get('end_date' , instance.end_date)
    #     instance.maximum_member_count = validated_data.get('maximum_member_count' , instance.maximum_member_count)
    #     instance.open_status = validated_data.get("open_status" , instance.open_status)
        
    #     instance.save()
        
    #     return instance


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']



