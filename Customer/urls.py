from django.urls import path
from .views import CustomerProfileView


urlpatterns = [
    # path("test/", CustomerProfileView.as_view(), name="customer_profile"),
    # path("customer/", "hi"),
    path('info/<int:pk>/',CustomerProfileView.as_view(),name='customer_profile')
    ]