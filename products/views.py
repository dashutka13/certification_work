from products.serializers import ProductSerializer
from products.models import Product
from users.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrStaff

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrStaff, IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Создание товара и определение владельца для него.
        """
        product = serializer.save()
        product.owner = get_object_or_404(User, id=self.request.user.id)
        product.save()
