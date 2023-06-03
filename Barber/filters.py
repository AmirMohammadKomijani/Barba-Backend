from django_filters.rest_framework import FilterSet,DateFromToRangeFilter
from .models import Barber,OrderServices




class BarberRateFilter(FilterSet):
    class Meta:
        model = Barber
        fields = {
            'area':['exact'],
            'rate':['gte','lte']
        }



class BarberPanelFilter(FilterSet):
    date = DateFromToRangeFilter()
    
    class Meta:
        model = OrderServices
        fields = ['status','date']
