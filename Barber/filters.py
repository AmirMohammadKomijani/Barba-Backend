from django_filters.rest_framework import FilterSet
from .models import Barber


class BarberRateFilter(FilterSet):
    class Meta:
        model = Barber
        fields = {
            'area':['exact'],
            'rate':['gte','lte']
        }