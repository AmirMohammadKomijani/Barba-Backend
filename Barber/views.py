from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Barber,Rate
from Auth.models import User
from .serializers import BarberSerializer,BarberProfileSerializer,RateSerializer
from .filters import BarberRateFilter
from rest_framework.permissions import IsAuthenticated




class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']
    permission_classes = [IsAuthenticated]



class BarberProfileView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (barber, created) = Barber.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = BarberProfileSerializer(barber)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BarberProfileSerializer(barber, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)





# class BarberShopImagesView(ModelViewSet):
#     serializer_class = BarberShopImagesSerializer

#     def get_serializer_context(self):
#         return {'barbershop_id':self.kwargs['barbershop_pk']}

#     def get_queryset(self):
#         return BarberShopImages.objects.filter(barbershop_id=self.kwargs['barbershop_pk'])



# class BarberView(ModelViewSet):
#     queryset = Barber.objects.all()
#     serializer_class = BarberSerializer


class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
