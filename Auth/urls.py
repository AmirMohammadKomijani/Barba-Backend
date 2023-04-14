from django.urls import path,include
from .views import CustomerRegisterView,BarberRegisterView,CustomerLoginView,BaberLoginView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
 
    path('customer/signup/', CustomerRegisterView.as_view(), name='signup'),
    path('barber/signup/', BarberRegisterView.as_view(), name='signup'),
    path('customer/login/', CustomerLoginView.as_view(), name='token-obtain-pair'),
    path('barber/login/', BaberLoginView.as_view(), name='token-obtain-pair'),
]
