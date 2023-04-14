from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView,CreateAPIView
from .models import Barber, Comment
from Auth.models import Barber as BarberModel_Auth 
from .serializers import BarberSerializer, BarberWithCommentsSerializer, CommentSerializer,CommentSerializerOnPOST
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Barber,BarberShopImages,Rate
from .serializers import BarberSerializer,BarberShopImagesSerializer,RateSerializer
from .filters import BarberRateFilter



class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    pagination_class = PageNumberPagination
    search_fields = ['BarberShop']
    ordering_fields = ['rate']


class BarberShopImagesView(ModelViewSet):
    serializer_class = BarberShopImagesSerializer

    def get_serializer_context(self):
        return {'barbershop_id':self.kwargs['barbershop_pk']}

    def get_queryset(self):
        return BarberShopImages.objects.filter(barbershop_id=self.kwargs['barbershop_pk'])



class BarberDetail(ListCreateAPIView):
    queryset = BarberModel_Auth.objects.all() #applied no filters yet!
    serializer_class = BarberWithCommentsSerializer
    
class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all() 
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializerOnPOST
        return CommentSerializer


class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer