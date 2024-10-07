from django.urls import path

from suppliers.views import SupplierListAPIView, SupplierCreateAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView
from suppliers.apps import SuppliersConfig

app_name = SuppliersConfig.name

urlpatterns = [
    path('', SupplierListAPIView.as_view(), name='supplier_list'),
    path('create/', SupplierCreateAPIView.as_view(), name='provider_create'),
    path('<int:pk>/', SupplierRetrieveAPIView.as_view(), name='provider_detail'),
    path('update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='provider_update'),
    path('delete/<int:pk>/', SupplierDestroyAPIView.as_view(), name='provider_delete'),
]
