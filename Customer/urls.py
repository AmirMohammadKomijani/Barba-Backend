from django.urls import path
from .views import CustomerProfileView
from rest_framework import routers



router = routers.SimpleRouter()
router.register('profile',CustomerProfileView,basename='profile')
# barber_router.register('images',views.BarberShopImagesView,basename='images')

urlpatterns = router.urls