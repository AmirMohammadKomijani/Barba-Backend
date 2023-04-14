from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group,Permission,AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
  
  Gender_Choices = [
    ('M','Male'),
    ('F','Female'),
  ]
  
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone_Number = models.CharField(max_length=11,unique=True)
  email = models.EmailField(unique=True)
  gender = models.CharField(max_length=6,choices=Gender_Choices)
  profile_picture = models.ImageField(null=True,error_messages={'invalid':"Image files only"},upload_to='profile_pictures/',blank=True,default="/default_profile.png")
  password = models.CharField(max_length=255)
  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['first_name', 'last_name']
    
  groups = models.ManyToManyField(
        Group,
        related_name='customer_groups'
    )
  user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_user_permissions'
    )
  

    
    
class Barber(AbstractBaseUser, PermissionsMixin):
  BarberShop = models.CharField(max_length=255)
  Owner = models.CharField(max_length=255)
  Parvaneh = models.CharField(max_length=10,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True)
  email = models.EmailField(unique=True)
  address = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  objects = CustomUserManager()

  USERNAME_FIELD = 'email'


  groups = models.ManyToManyField(
        Group,
        related_name='barber_groups'
    )
  user_permissions = models.ManyToManyField(
        Permission,
        related_name='barber_user_permissions'
    )

