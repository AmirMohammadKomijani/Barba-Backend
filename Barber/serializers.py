from rest_framework import serializers
from .models import Barber,OrderServices,CategoryService,Category,BarberDescription, Comment,BarberPremium, Rating
from Auth.serializers import UserSerializer
from Customer.serializers import  CustomerWalletSerializer
from Customer.models import Customer
from dateutil.relativedelta import relativedelta
import datetime
from rest_framework.response import Response



class RatingSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.id')
    barber = serializers.ReadOnlyField(source='barber.id')

    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ("id", "created_at", "barber", "customer")
        # exclude = ("created_at",)
        
    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance

#######################################################
### Barber Panel Serializers

##############################################################
##### Bad Copy
class InfoCategoryServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = CategoryService
        fields = ['id','service','price','servicePic']

    def create(self, validated_data):
        category = Category.objects.get(id = self.context['category_id'])
        validated_data['category'] = category
        return CategoryService.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.service = validated_data.get('service',instance.service)
        instance.price = validated_data.get('price',instance.price)
        instance.servicePic = validated_data.get('servicePic',instance.servicePic)
        instance.save()
        return instance
         
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['servicePic'] = "https://amirmohammadkomijani.pythonanywhere.com" + representation['servicePic']
    #     return representation
    
class InfoCategorySerializer(serializers.ModelSerializer):
    categoryServices = InfoCategoryServiceSerializer(many=True,read_only=True)
    class Meta():
        model = Category
        fields = ['id','category','categoryServices']
    
    def create(self, validated_data):
        barber = Barber.objects.get(user_id = self.context['barber_id'])
        validated_data['barber'] = barber
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category',instance.category)
        instance.save()
        return instance


############################################################

## 1/ adding category and service

class CategoryServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = CategoryService
        fields = ['id','service','price','servicePic']

    def create(self, validated_data):
        category = Category.objects.get(id = self.context['category_id'])
        validated_data['category'] = category
        return CategoryService.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.service = validated_data.get('service',instance.service)
        instance.price = validated_data.get('price',instance.price)
        instance.servicePic = validated_data.get('servicePic',instance.servicePic)
        instance.save()
        return instance
         
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['servicePic'] = "https://amirmohammadkomijani.pythonanywhere.com" + representation['servicePic']
        return representation
    
class CategorySerializer(serializers.ModelSerializer):
    categoryServices = CategoryServiceSerializer(many=True,read_only=True)
    class Meta():
        model = Category
        fields = ['id','category','categoryServices']
    
    def create(self, validated_data):
        barber = Barber.objects.get(user_id = self.context['barber_id'])
        validated_data['barber'] = barber
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category',instance.category)
        instance.save()
        return instance

## 2/ profile and description of barbershop

class BarberDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberDescription
        fields = ['id','title','description','img']

    def create(self, validated_data):
        barber = Barber.objects.get(user_id = self.context['barber_id'])
        validated_data['barber'] = barber
        return BarberDescription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.img = validated_data.get('img',instance.img)
        instance.save()
        return instance
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['img'] = "https://amirmohammadkomijani.pythonanywhere.com" + representation['img']
        return representation


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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['background'] = "https://amirmohammadkomijani.pythonanywhere.com" + representation['background']
        representation['logo'] = "https://amirmohammadkomijani.pythonanywhere.com" + representation['logo']
        return representation



## 3/ Barber management segment

class CustomerInfoBarberPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','first_name','last_name','profile_pic']


class Get_BarberPanelSerializer(serializers.ModelSerializer):
    service = CategoryServiceSerializer()
    customer = CustomerInfoBarberPanelSerializer()
    originalPrice = serializers.SerializerMethodField(method_name='original_price')
    totalCost = serializers.SerializerMethodField(method_name='total')
    class Meta:
        model = OrderServices
        fields = ['id','service','customer', 'time','date','status','quantity','originalPrice','totalCost']

    def original_price(self,obj):
        return obj.service.price
    
    def total(self,obj):
        return obj.service.price * obj.quantity

    
class Put_BarberPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderServices
        fields = ['status']

    def update(self, instance, validated_data):
        if instance.status == "ordering" and instance.date >= datetime.date.today():
            instance.status = validated_data.get('status',instance.status)
        instance.save()
        return instance


class GetBarberPremiumSerializer(serializers.ModelSerializer):

    # month = serializers.ChoiceField(choices=Months_choices)
    days = serializers.SerializerMethodField(method_name='calc_days')
    class Meta:
        model = BarberPremium
        fields = ['id','expire_date','month','days']
    
    def calc_days(self,obj):
        days = (obj.expire_date - datetime.date.today()).days
        if days >= 0:
            return days
        return 0
 


class PutBarberPremiumSerializer(serializers.ModelSerializer):

    # month = serializers.ChoiceField(choices=Months_choices)
    # days = serializers.SerializerMethodField(method_name='calc_days')
    class Meta:
        model = BarberPremium
        fields = ['id','expire_date','month']
    
    # def calc_days(self,obj):
    #     return (obj.expire_date - datetime.date.today()).days
    
    def update(self, instance, validated_data):
        # instance.expire_date = validated_data.get('expire_date',instance.expire_date)
        if instance.expire_date <= datetime.date.today():
            instance.month = validated_data.get('month',instance.month)
            instance.expire_date += relativedelta(months=instance.month)
            instance.save()
            return instance
        # elif instance.expire_date - datetime.date.today() < 0:
        #     return Response({"message":"wrong"})
        else:
            return 0
    
    
    

# Comment Serializer; allow customer to post a comment
class CommentSerializerOnPOST(serializers.ModelSerializer):
    # customer = CustomerWalletSerializer(read_only = True)
    # customer = serializers.SerializerMethodField()
    # replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ("id", "barber", "body", "created_at",)
    
    def create(self, validated_data):
        (customer,created) = Customer.objects.get_or_create(user_id = self.context['customer_id'])
        validated_data['customer'] = customer
        return Comment.objects.create(**validated_data)
        # read_only_fields = ("id", "created_at","customer" )
        # exclude = ("created_at")
    # def get_replies(self, obj):
    #     replies = obj.replies.all()
    #     serializer = self.__class__(replies, many=True, context=self.context)
    #     return serializer.data        

    # def create(self, validated_data):
    #     validated_data['customer'] = self.context['request'].user.customer
    #     return super().create(validated_data)
    # def get_customer(self, obj):
    #     customer = obj.customer
    #     serializer = CustomerWalletSerializer(customer, many=False, context=self.context)
    #     return serializer.data
class CommentSerializerOnGET(serializers.ModelSerializer):
    customer = CustomerWalletSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id", "created_at",)
        
class CommentSerializerOnPUT(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',"body", 'reply', 'created_at')
        read_only_fields = ('id', 'created_at',"body")
################################################################

### customer ordering and paying process
## 1/ Barber info

class BarberInfoDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberDescription
        fields = ['id','title','description','img']
    
class BarberInfoSerializer(serializers.ModelSerializer):
    categories = InfoCategorySerializer(many=True)
    rating = serializers.SerializerMethodField(source= "get_rating")
    customers_rate = serializers.SerializerMethodField()
    barberDesc = BarberInfoDescriptionSerializer(many=True)
    comments = CommentSerializerOnGET(many=True,) 
    class Meta:
        model = Barber
        fields = ['id','BarberShop','Owner','phone_Number','area','address','rate','background','logo','categories','barberDesc',
                  "rating", "customers_rate", "comments"]

    def get_rating(self,obj):
        ratings = obj.ratings.all()
        if ratings :
            ratings = [rating_instance.rating for rating_instance in ratings]
            # print(*ratings, sep = "\*n")
            return round(sum(ratings) / len(ratings), 2)
        else:
            return 0.00
    def get_customers_rate(self, obj):
        customer = self.context['request'].user.customer
        # print(customer, sep = "*****\n")
        try:
            rating = obj.ratings.filter(customer=customer).order_by("-created_at").first()
            # rating = Rating.objects.get(customer= customer, barber = obj)
            return rating.rating
        except:
            return None
            
## 2/ Ordering a service

class OrderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderServices
        fields = ['id','service','barber', 'time','date','status']

        
    def save(self, **kwargs):
        (customer, created) = Customer.objects.get_or_create(user_id=self.context['user_id'])
        self.validated_data.update({'customer':customer,**kwargs})
        order = OrderServices.objects.create(**self.validated_data)
        return order


## 3/ Customer Basket

class BarberBasketInfoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Barber
        fields = ['BarberShop','phone_Number','area','address','logo']

class Get_CustomerBasketSerializer(serializers.ModelSerializer):
    service = InfoCategoryServiceSerializer()
    barber = BarberBasketInfoSerializer()
    originalPrice = serializers.SerializerMethodField(method_name='original_price')
    totalCost = serializers.SerializerMethodField(method_name='total')
    class Meta():
        model = OrderServices
        fields = ['id','service','barber', 'time','date','status','quantity','originalPrice','totalCost']

    def original_price(self,obj):
        return obj.service.price
    
    def total(self,obj):
        return obj.service.price * obj.quantity
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status',instance.status)
        instance.save()
        return instance
    
class Put_CustomerBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderServices
        fields = ['status','quantity']
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status',instance.status)
        instance.quantity = validated_data.get('quantity',instance.quantity)
        instance.save()
        return instance


###############################################################
### extra information    

class BarberAreasSerializer(serializers.ModelSerializer):
    class Meta():
        model = Barber
        fields = ['area']
