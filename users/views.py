from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer, AdminUserSerializer


class UserListAPIView(generics.ListAPIView):
    """ Контроллер для вывода списка пользователей """
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]


class UserCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания пользователей """
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        new_user = serializer.save(is_active=True)
        new_user.set_password(new_user.password)
        new_user.save()


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ Контроллер для просмотра и редактирования пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]
