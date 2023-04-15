from django.urls import path
from . import views
## when we use ModelViewSet we should implement urls with routers
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('info',views.BarberView,basename='info')


barber_router = routers.NestedDefaultRouter(router,'info',lookup='barbershop')
# barber_router.register('images',views.BarberShopImagesView,basename='images')

urlpatterns = router.urls + barber_router.urls

# router = DefaultRouter()
# router.register('info',views.BarberView)
# router.register('info/<int:pk>/images/',views.BarberShopImagesView,basename='barber-image')
# router.register('rate',views.RateView)

# urlpatterns = router.urls


# urlpatterns = [
#     path('info/<int:pk>/images',views.BarberView.as_view(),name='Barber info'),
#     path('info/',views.BarberShopImagesView.as_view(),name='Barbers info'),
#     path('rate/<int:pk>/',views.RateView.as_view(),name = 'Rate Barber'),
# ]