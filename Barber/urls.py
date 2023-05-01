from django.urls import path
from . import views
## when we use ModelViewSet we should implement urls with routers
from rest_framework_nested import routers as nested
from rest_framework import routers 



nestedRouter = nested.DefaultRouter()
router = routers.SimpleRouter()

nestedRouter.register('info',views.BarberView,basename='info')
router.register('profile',views.BarberProfileView,basename='profile')
# router.register('category',views.addCategory)
# router.register('service',views.addService,basename='add service')
router.register('area',views.Areas,basename='show areas')
router.register('order',views.OrderServiceView,basename='order')



nestedRouter.register('categories', views.addCategoryView, basename='categories')
service_router = nested.NestedSimpleRouter(nestedRouter, 'categories', lookup='category')
service_router.register('service', views.addCategoryServiceView, basename='services')



urlpatterns = router.urls + nestedRouter.urls + service_router.urls

