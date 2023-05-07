from django.db import models
from django.conf import settings
from Auth.models import User
# from ..Auth.models import Customer
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    area = models.CharField(max_length=255,null=True)
    phone_Number = models.CharField(max_length=11,unique=True,null=True)
    profile_pic = models.ImageField(upload_to='customer/profile',null=False,default='default_profile.png')
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)