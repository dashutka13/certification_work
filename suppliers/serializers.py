from rest_framework import serializers
from products.serializers import ProductSerializer
from suppliers.models import Supplier


class RetailSerializerView(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ['debt']
