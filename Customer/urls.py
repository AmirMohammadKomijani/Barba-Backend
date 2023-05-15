from django.urls import path
from .views import CustomerProfileView,WalletView
from rest_framework import routers



router = routers.SimpleRouter()
router.register('profile',CustomerProfileView,basename='profile')
router.register('wallet',WalletView,basename='wallet')
# barber_router.register('images',views.BarberShopImagesView,basename='images')

urlpatterns = router.urls