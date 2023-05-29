from django.db import models
from django.conf import settings
from Auth.models import User
from Customer.models import Customer
import datetime
from dateutil.relativedelta import relativedelta



class Barber(models.Model):

  area_chices = (
    ('Tehranpars','Tehranpars'),
    ('Nazi Abad','Nazi Abad'),
    ('Narmak','Narmak'),
    ('Tajrish','Tajrish'),
    ('Gheytariye','Gheytariye'),
    ('Marzdaran','Marzdaran'),
    ('Janat Abad','Janat Abad'),
    ('Vanak','Vanak'),
    ('Enghelab','Enghelab'),
    ('Valiasr','Valiasr'),
    ('Saadat Abad','Saadat Abad'),
    ('Piroozi','Piroozi'),
    ('Jordan','Jordan'),
  )

  user = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='users',null=False)
  BarberShop = models.CharField(max_length=255,unique=False,null=False)
  Owner = models.CharField(max_length=255,null=False)
  Parvaneh = models.CharField(max_length=10,unique=True,null=True)
  phone_Number = models.CharField(max_length=11,unique = True,null=True)
  area = models.CharField(max_length=255,null=False,choices=area_chices)
  address = models.CharField(max_length=255,null=False)
  rate = models.FloatField(default=1,null=False)
  background = models.ImageField(upload_to='Barber/backg',null=False,default='default_profile.png')
  logo = models.ImageField(upload_to='Barber/Logo',null=False,default='default_profile.png')
  # expire_date = models.DateField(default=datetime.date.today() + relativedelta(months=1))

  # def save(self, *args, **kwargs):
  #     if not self.expire_date:
  #         self.expire_date = User.date_joined + relativedelta(months=1)
  #     super(Barber, self).save(*args, **kwargs)


class BarberDescription(models.Model):
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='barberDesc',null=True)
  title = models.CharField(max_length=40)
  description = models.TextField(max_length=256)
  img = models.ImageField(upload_to='Barber/Description',null=False,default='default_profile.png')


class BarberPremium(models.Model):
    
  during_choices = (
    (1,'1-month'),
    (3,'3-month'),
    (6,'6-month'),
    (12,'12-month'),
  )
  
  
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,default=1)
  expire_date = models.DateField(default=datetime.date.today() + relativedelta(months=1))
  month = models.IntegerField(choices=during_choices,default=0)


class Category(models.Model):
  
  # catg_choices = (
  #   ('hair','hair'),
  #   ('skin','skin'),
  #   ('makeup','makeup'),
  #   ('nail','nail'),
  # )
  
  category = models.CharField(max_length=20,null=False)
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,null=True,related_name='categories')


class CategoryService(models.Model):
  service = models.CharField(max_length=255,null=False)
  price = models.FloatField(null=False)
  servicePic = models.ImageField(upload_to='Barber/Service',null=True,default='default_profile.png')
  category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categoryServices')


class OrderServices(models.Model):
  
  order_status = (
    ('ordering','ordering'),
    # ('ordered','ordered'),
    # ('confirmed','confirmed'),
    ('paid','paid'),
    ('BarberCancelled','BarberCancelled'),
    ('CustomerCancelled','CustomerCancelled'),
    ('CustomerNotCome','CustomerNotCome'),
    ('Done','Done'),
  )
  
  service = models.ForeignKey(CategoryService,on_delete=models.CASCADE,related_name='services')
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='barber')
  time = models.TimeField()
  date = models.DateField(default=datetime.date.today)
  status = models.CharField(max_length=20,choices=order_status,default='ordering')
  quantity = models.IntegerField(default=1)
  # totalPrice = models.FloatField(default=0)
  
  class Meta:
      unique_together = ('barber', 'time','date')
      ordering = ['date','time']


class Comment(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="authors_comments")
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE, related_name="comments")
  body = models.TextField(max_length=1000,)
  reply = models.TextField(max_length=1000,null=True, blank=True, default=None)
  created_at = models.DateTimeField(auto_now_add=True)
  # parent_comment = models.ForeignKey("self", null=True, default=None, on_delete=models.CASCADE, related_name="replies")
  class Meta:
    ordering = ['-created_at']
  def __str__(self):
    return f'{self.customer} Says:{self.body}; Reply:{self.reply}'  
  # @property
  # def children(self):
      # return Comment.objects.filter(parent_comment=self).reverse()
  # @property
  # def is_parent(self):
  #     if self.parent_comment is None:
  #         return True
  #     return False







