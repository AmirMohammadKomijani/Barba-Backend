from django.urls import path
from .views import BarberView, BarberDetail, CommentView
from rest_framework_nested import routers


urlpatterns = [
    path("info2/<int:pk>/",BarberDetail.as_view(), name="Barber info with comments"),
    path("comments/", CommentView.as_view(), name="all_comments"),
]

## when we use ModelViewSet we should implement urls with routers


router = routers.DefaultRouter()
router.register('info',BarberView,basename='info')


barber_router = routers.NestedDefaultRouter(router,'info',lookup='barbershop')
# barber_router.register('images',views.BarberShopImagesView,basename='images')

urlpatterns += router.urls + barber_router.urls

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