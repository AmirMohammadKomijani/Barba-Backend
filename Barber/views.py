from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Barber,Rate,Service
from .serializers import BarberSerializer,BarberProfileSerializer,RateSerializer,ServiceSerializer,CreateServiceSerializer,BarberAreasSerializer
from .filters import BarberRateFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Auth.models import User




class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']
    # permission_classes = [IsAuthenticated]


class BarberProfileView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberProfileSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (barber, created) = Barber.objects.get_or_create(
            user_id=request.user.id)
        # baseInfo = User.objects.prefetch_related('barber_set').all()
        if request.method == 'GET':
            serializer = BarberProfileSerializer(barber)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BarberProfileSerializer(barber, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class Areas(ModelViewSet):
    serializer_class = BarberAreasSerializer

    def get_queryset(self):
        return Barber.objects.only('area')



# class addService(APIView):
#     def post(self,request):
#         barber = Barber.objects.get(id = request.user.id)
#         serializer = ServiceSerializer(data=request.data)
#         if serializer.is_valid():
#             service = serializer.save(barber=barber)           
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class addService(ModelViewSet):
    # queryset = Service.objects.all()
    # serializer_class = ServiceSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateServiceSerializer
        return ServiceSerializer

    def get_queryset(self):
        (barber,created) = Barber.objects.only('id').get_or_create(user_id = self.request.user.id)
        return Service.objects.filter(barber_id = barber).all()
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}




# class addService(ListCreateAPIView):
#     serializer_class = ServiceSerializer
#     # permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             # retrieve all services for the authenticated barber
#             return Service.objects.filter(barber_id=self.request.user.barber.id)
#         else:
#             return Service.objects.none()
    
#     def perform_create(self, serializer):
#         # create a new service row in the database for the authenticated barber
#         serializer.save(barber_id=self.request.user.barber.id)



# class addService(ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer






# class addCategory(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class addService(ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     # # permission_classes = [IsAuthenticated]
    
# #     def list(self,request):
# #         serv=Service.objects.all()
# #         serializer=ServiceSerializer(serv,many=True)
# #         return Response(serializer.data)
    
# #     def create(self,request):
# #         serializer=ServiceSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response({'msg':'Data  created'}, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=False,methods=['GET','POST'], permission_classes = [IsAuthenticated])
#     def add(self,request):
#         barber = Service.objects.get(barber_id=request.user.barber.id)

#         if request.method == 'GET':
#             serializer = ServiceSerializer(barber,many=True)
#             return Response(serializer.data)
#         # elif request.method == 'PUT':
#         #     serializer = ServiceSerializer(barber, data=request.data)
#         #     serializer.is_valid(raise_exception=True)
#         #     serializer.save()
#         #     return Response(serializer.data)
#         elif request.method == 'POST':
#             serializer = ServiceSerializer(barber, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
 

# class BarberManagement(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     @action(detail=False,methods=['GET','PUT','POSt'], permission_classes = [IsAuthenticated])
#     def addService(self,request):
#         barber = Barber.objects.get(id = request.user.id)

#         if request.method == 'GET':
#             serializer = CategorySerializer(barber)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = CategorySerializer(barber,data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
#         elif request.method == 'POST':
#             serializer = CategorySerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)


        
class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer



