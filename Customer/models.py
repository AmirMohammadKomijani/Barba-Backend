from django.db import models
# from ..Auth.models import Customer
# Create your models here.

class CustomerProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_Number = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True)
    