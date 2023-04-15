from django.db import models

  
class Rate(models.Model):
  barbershop = models.ForeignKey('Barber',on_delete=models.SET_NULL,null=True,related_name='barbers')
  stars = models.IntegerField()

class Barber(models.Model):
  BarberShop = models.CharField(max_length=255,unique=True)
  Owner = models.CharField(max_length=255)
  Parvaneh = models.CharField(max_length=10,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True)
  email = models.EmailField(unique=True)
  address = models.CharField(max_length=255)
  rate = models.FloatField(default=1)

class BarberShopImages(models.Model):
  barbershop = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='images')
  background = models.ImageField(upload_to='Barber/backg')
  logo = models.ImageField(upload_to='Barber/Logo')



