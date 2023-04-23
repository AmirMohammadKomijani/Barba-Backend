from django.db import models
from django.conf import settings
from Auth.models import User

  
class Rate(models.Model):
  barbershop = models.ForeignKey('Barber',on_delete=models.SET_NULL,null=True,related_name='barbers')
  stars = models.IntegerField()

class Barber(models.Model):
  user = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='users',null=False)
  BarberShop = models.CharField(max_length=255,unique=True,null=False)
  Owner = models.CharField(max_length=255,null=False)
  Parvaneh = models.CharField(max_length=10,unique=True,null=False)
  phone_Number = models.CharField(max_length=11,unique = True,null=False)
  # email = models.EmailField(unique=True)
  area = models.CharField(max_length=255,null=False)
  address = models.CharField(max_length=255,null=False)
  rate = models.FloatField(default=1,null=False)
  background = models.ImageField(upload_to='Barber/backg',null=False,default='default_profile.png')
  logo = models.ImageField(upload_to='Barber/Logo',null=False,default='default_profile.png')



# class Category(models.Model):
  
#   catg_choices = (
#     ('hair','hair'),
#     ('skin','skin'),
#     ('makeup','makeup'),
#     ('nail','nail'),
#   )
  
#   category = models.CharField(choices=catg_choices,max_length=20)
#   barber = models.ForeignKey(Barber,on_delete=models.CASCADE,null=True,related_name='categories')


class Service(models.Model):
  catg_choices = (
    ('hair','hair'),
    ('skin','skin'),
    ('makeup','makeup'),
    ('nail','nail'),
    )
  
  service = models.CharField(blank=True,max_length=255)
  price = models.FloatField(default=0)
  service_pic = models.ImageField(upload_to='Barber/Service',null=True,default='default_profile.png')
  category = models.CharField(choices=catg_choices,max_length=20)
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='services',null=False,unique=False)
  # catg = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='services')









# class BarberShopImages(models.Model):
#   barbershop = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='images')
#   background = models.ImageField(upload_to='Barber/backg')
#   logo = models.ImageField(upload_to='Barber/Logo')



