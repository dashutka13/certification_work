import django_filters
from suppliers.models import Supplier


class SupplierFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Supplier
        fields = ['country']
