from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Barber,BarberDescription,BarberPremium

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_barber_for_new_user(sender, **kwargs):
  if kwargs['created'] and kwargs['instance'].role == 'barber':
    Barber.objects.create(user=kwargs['instance'])



@receiver(post_save, sender=Barber)
def create_barber_for_new_user(sender, **kwargs):
  if kwargs['created']:
    BarberDescription.objects.create(barber=kwargs['instance'])
    BarberPremium.objects.create(barber=kwargs['instance'])