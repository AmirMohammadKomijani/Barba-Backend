from rest_framework import serializers
from .models import Barber,Rate,OrderServices,CategoryService,Category
from Auth.serializer import UserSerializer
from Customer.serializers import CustomerSerializer
from Customer.models import Customer



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


class CategoryServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = CategoryService
        fields = ['id','service','price','servicePic']
    
    def save(self, **kwargs):
        (category,created) = Category.objects.get_or_create(id = self.context['category_id'])
        self.validated_data.update({'category':category,**kwargs})
        service = CategoryService.objects.create(**self.validated_data)
        return service


class CategorySerializer(serializers.ModelSerializer):
    categoryServices = CategoryServiceSerializer(many=True,read_only=True)
    class Meta():
        model = Category
        fields = ['id','category','categoryServices']
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category',instance.category)
        instance.save()
        return instance
    
    def save(self, **kwargs):
        (barber,created) = Barber.objects.get_or_create(id=self.context['barber_id'])
        self.validated_data.update({'barber':barber,**kwargs})
        catg = Category.objects.create(**self.validated_data)
        return catg

class CustomerBasketSerializer(serializers.ModelSerializer):
    service = CategoryServiceSerializer()
    barber = BasketBarberInfoSerializer()
    class Meta():
        model = OrderServices
        fields = ['id','service','barber', 'time','date','status']

    
    
class BarberSerializer(serializers.ModelSerializer):
    # services = ServiceSerializer(many=True)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Barber
        fields = ['id','BarberShop','Owner','phone_Number','area','address','rate','background','logo','categories']


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
        fields = ['id','full_name','profile_pic']

        
class BarberPanelSerializer(serializers.ModelSerializer):
    service = ServiceBarberPanelSerializer()
    customer = CustomerInfoBarberPanelSerializer()
    class Meta:
        model = OrderServices
        fields = ['id','service','customer','date','time','status']




    



