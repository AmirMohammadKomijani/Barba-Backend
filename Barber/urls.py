from django.urls import path
from . import views
## when we use ModelViewSet we should implement urls with routers
from rest_framework_nested import routers as nested
from rest_framework import routers 



nestedRouter = nested.DefaultRouter()
router = routers.SimpleRouter()

nestedRouter.register('info',views.BarberView,basename='info')
router.register('profile',views.BarberProfileView,basename='profile')


barber_info = nested.NestedDefaultRouter(nestedRouter,'info',lookup='barbershop')

# barber_router.register('images',views.BarberShopImagesView,basename='images')

urlpatterns = router.urls + barber_info.urls + nestedRouter.urls

