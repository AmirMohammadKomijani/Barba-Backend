from rest_framework import serializers
from Auth.models import Barber as BarberModel_Auth, Customer
from .models import Barber,BarberShopImages,Rate, Comment


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
        fields = ['id','BarberShop','Owner','phone_Number','address',"rate",'images']



class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']
    
    

class CustomerSerializer(serializers.ModelSerializer): 
    # Serializer for the customer field in the Comment model
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "profile_picture")

class CommentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Comment
        fields = "__all__"
class CommentSerializerOnPOST(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        exlude = ("created_at",)
    
        
class BarberWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True)
    class Meta:
        model = BarberModel_Auth
        fields =['BarberShop','Owner','phone_Number','address', "comments"]
        read_only_fields = ( "created_at",) 