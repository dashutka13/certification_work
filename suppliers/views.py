from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from suppliers.models import Supplier
from suppliers.serializers import RetailSerializerView, SupplierSerializer, SupplierSerializerUpdate
from users.permissions import IsOwnerOrStaff


class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = RetailSerializerView
    permission_classes = [IsAuthenticated, ]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = RetailSerializerView
    permission_classes = [IsAuthenticated]


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_provider = serializer.save()
        new_provider.author = self.request.user
        new_provider.save()


class SupplierUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SupplierSerializerUpdate
    queryset = Supplier.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]

class SupplierDestroyAPIView(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    permission_classes = [IsOwnerOrStaffgit , IsAuthenticated]
    serializer_class = SupplierSerializer
