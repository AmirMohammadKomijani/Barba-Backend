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
router.register('service',views.addService,basename='add service')
router.register('area',views.Areas,basename='show areas')
router.register('order',views.OrderServiceView,basename='order')



# router.register('baseprofile',views.BarberBaseProfileView,basename='Base-profile')
# urlpatterns = [
#             # path('baseprofile/<int:pk>',views.BarberBaseProfileView.as_view()),
#             #path('baseprofile/<int:pk>',views.BarberBaseProfileView.as_view()),
# ]
# urlpatterns = [
#         # path('baseprofile/',views.BarberBaseProfileView.as_view()),
#         path('add/',views.addService.as_view())
# ]

#-----
# barber_service = nested.NestedDefaultRouter(nestedRouter,'info',lookup='info')
# barber_service.register('services',views.OrderServiceView,basename = 'order service')

# barber_router.register('images',views.BarberShopImagesView,basename='images')

urlpatterns = router.urls + nestedRouter.urls #+ barber_service.urls

