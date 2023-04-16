from django.db import models
from django.conf import settings
from Auth.models import User

  
class Rate(models.Model):
  barbershop = models.ForeignKey('Barber',on_delete=models.SET_NULL,null=True,related_name='barbers')
  stars = models.IntegerField()

class Barber(models.Model):
  user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  BarberShop = models.CharField(max_length=255,unique=True)
  Owner = models.CharField(max_length=255)
  Parvaneh = models.CharField(max_length=10,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True)
  # email = models.EmailField(unique=True)
  area = models.CharField(max_length=255,default=' ')
  address = models.CharField(max_length=255)
  rate = models.FloatField(default=1)
  background = models.ImageField(upload_to='Barber/backg',null=True)
  logo = models.ImageField(upload_to='Barber/Logo',null=True)


# class BarberShopImages(models.Model):
#   barbershop = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='images')
#   background = models.ImageField(upload_to='Barber/backg')
#   logo = models.ImageField(upload_to='Barber/Logo')



