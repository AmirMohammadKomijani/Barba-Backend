from django_filters.rest_framework import FilterSet,DateFromToRangeFilter
from .models import Barber,CategoryService,OrderServices


class BarberRateFilter(FilterSet):
    class Meta:
        model = Barber
        fields = {
            'area':['exact'],
            'rate':['gte','lte']
        }

class BarberPanelFilter(FilterSet):
    #price = RangeFilter()
    # price = NumberFilter(method='priceRange')

    # def priceRange(self):
    #     service_id = OrderServices.objects.get(id = self.request.user.id)
    #     return CategoryService.objects.only('price').filter(id = service_id)

    date = DateFromToRangeFilter()

    class Meta:
        model = OrderServices
        fields = ['status','date']