from django.db import models
from django.contrib.auth.models import Group,Permission,AbstractUser


class User(AbstractUser):

    choice_field = (
        ('barber','barber'),
        ('customer','customer'),
    )

    role = models.CharField(choices=choice_field,max_length=8)
    email = models.EmailField(unique=True)
    username = models.CharField(default='user',null=True,max_length=20,unique=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['role','username','password']

        
    groups = models.ManyToManyField(
        Group,
        related_name='customer_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_user_permissions'
    )
  












# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group,Permission,AbstractUser
# from django.db import models


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Email field is required')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class Customer(AbstractBaseUser, PermissionsMixin):
  
#   Gender_Choices = [
#     ('M','Male'),
#     ('F','Female'),
#   ]
  
#   first_name = models.CharField(max_length=255)
#   last_name = models.CharField(max_length=255)
#   phone_Number = models.CharField(max_length=11,unique=True)
#   email = models.EmailField(unique=True)
#   gender = models.CharField(max_length=6,choices=Gender_Choices)
#   password = models.CharField(max_length=255,unique=True)
#   objects = CustomUserManager()

# #   USERNAME_FIELD = 'email'
# #   REQUIRED_FIELDS = ['first_name', 'last_name']
    
#   groups = models.ManyToManyField(
#         Group,
#         related_name='customer_groups'
#     )
#   user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='customer_user_permissions'
#     )
  

    
    
# class Barber(AbstractBaseUser, PermissionsMixin):
#   BarberShop = models.CharField(max_length=255)
#   Owner = models.CharField(max_length=255)
#   Parvaneh = models.CharField(max_length=10,unique=True)
#   phone_Number = models.CharField(max_length=11,unique = True)
#   email = models.EmailField(unique=True)
#   address = models.CharField(max_length=255)
#   password = models.CharField(max_length=255,unique=True)
#   objects = CustomUserManager()

#   groups = models.ManyToManyField(
#         Group,
#         related_name='barber_groups'
#     )
#   user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='barber_user_permissions'
#     )

