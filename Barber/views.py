from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Barber,BarberShopImages,Rate
from .serializers import BarberSerializer,BarberShopImagesSerializer,RateSerializer
from .filters import BarberRateFilter



class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']


class BarberShopImagesView(ModelViewSet):
    serializer_class = BarberShopImagesSerializer

    def get_serializer_context(self):
        return {'barbershop_id':self.kwargs['barbershop_pk']}

    def get_queryset(self):
        return BarberShopImages.objects.filter(barbershop_id=self.kwargs['barbershop_pk'])



# class BarberView(ModelViewSet):
#     queryset = Barber.objects.all()
#     serializer_class = BarberSerializer


class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
