from rest_framework import serializers
from .models import Barber,Rate,OrderServices,CategoryService,Category,BarberDescription
from Auth.serializer import UserSerializer
from Customer.serializers import CustomerSerializer
from Customer.models import Customer



# class TotalPriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TotalPrice
#         fields = ['total']
    
    
    # def create(self, validated_data):
    #     # category = Category.objects.get(id = self.context['category_id'])
    #     # validated_data['category'] = category
    #     return TotalPrice.objects.create(**validated_data)

class BasketBarberInfoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Barber
        fields = ['BarberShop','phone_Number','area','address']


class OrderServiceSerializer(serializers.ModelSerializer):
    # service_id = serializers.PrimaryKeyRelatedField(source='service', queryset=Service.objects.all())

    class Meta:
        model = OrderServices
        fields = ['id','service','barber', 'time','date','status']

    
    # def validate_time(self, barber_id):
    #     if OrderServices.objects.filter(barber_id = barber_id):
    #         if OrderServices.objects.only('time').exists():
    #             raise ValueError('this time has been set')
    
    
    def save(self, **kwargs):
        customer, created = Customer.objects.get_or_create(user_id=self.context['user_id'])
        # barber, created = Barber.objects.get_or_create(id=self.context['barber_id'])
        # service, created = Service.objects.get_or_create(id=self.context['service_id'])
        # self.validated_data.update({'customer': customer,'barber':barber,'service':service, **kwargs})
        self.validated_data.update({'customer':customer,**kwargs})
        order = OrderServices.objects.create(**self.validated_data)
        return order

    # def create(self, validated_data):
    #     category = Category.objects.get(id = self.context['category_id'])
    #     validated_data['category'] = category
    #     return CategoryService.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.service = validated_data.get('service',instance.service)
    #     instance.price = validated_data.get('price',instance.price)
    #     instance.servicePic = validated_data.get('servicePic',instance.servicePic)
    #     instance.save()
    #     return instance


class CategoryServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = CategoryService
        fields = ['id','service','price','servicePic']
    
    # def save(self, **kwargs):
    #     (category,created) = Category.objects.get_or_create(id = self.context['category_id'])
    #     self.validated_data.update({'category':category,**kwargs})
    #     service = CategoryService.objects.create(**self.validated_data)
    #     return service

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
    
    # def save(self, **kwargs):
    #     (barber,created) = Barber.objects.get_or_create(id=self.context['barber_id'])
    #     self.validated_data.update({'barber':barber,**kwargs})
    #     catg = Category.objects.create(**self.validated_data)
    #     return catg

class Get_CustomerBasketSerializer(serializers.ModelSerializer):
    service = CategoryServiceSerializer()
    barber = BasketBarberInfoSerializer()
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

# class CustomerBasketTotalPriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderServices
#         fields = ['totalPrice']

class BarberDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberDescription
        fields = ['id','title','description','img']

    def create(self, validated_data):
        barber = Barber.objects.get(id = self.context['barber_id'])
        validated_data['barber'] = barber
        return BarberDescription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.img = validated_data.get('img',instance.img)
        instance.save()
        return instance
    
class BarberSerializer(serializers.ModelSerializer):
    # services = ServiceSerializer(many=True)
    categories = CategorySerializer(many=True)
    barberDesc = BarberDescriptionSerializer(many=True)
    class Meta:
        model = Barber
        fields = ['id','BarberShop','Owner','phone_Number','area','address','rate','background','logo','categories','barberDesc']


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
        # representation['first_name'] = representation['first_name']
        # representation['last_name'] = representation['last_name']
        # representation['phone_Number'] = representation['phone_Number']
        # representation['area'] = representation['area']
        # representation['user'] = representation['user']
        return representation


class BarberAreasSerializer(serializers.ModelSerializer):
    class Meta():
        model = Barber
        fields = ['area']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']



class ServiceBarberPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryService
        fields = ['id','service','price']


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

    # def update(self, instance, validated_data):
    #     instance.status = validated_data.get('status',instance.status)
    #     instance.save()
    #     return instance
    
class Put_BarberPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderServices
        fields = ['status']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status',instance.status)
        instance.save()
        return instance






# class CustomerBuyWalletSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['credit']
    
#     def update(self, instance, validated_data):
#         instance.credit = validated_data.get('credit',instance.credit)
#         instance.save()
#         return instance




    



