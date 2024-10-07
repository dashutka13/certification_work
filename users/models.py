from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import NULLABLE


class User(AbstractUser):
    ADMIN = "admin"
    USER = "user"
    USER_ROLES = ((ADMIN, "админ"), (USER, "пользователь") )
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    role = models.CharField(choices=USER_ROLES, default=USER, verbose_name='Роль пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('pk',)
