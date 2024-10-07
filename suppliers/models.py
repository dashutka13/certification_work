from django.db import models
from django.utils import timezone

from config.settings import NULLABLE
from users.models import User


class Supplier(models.Model):
    """Модель поставщика"""

    FACTORY = 0
    RETAILER = 1
    SP = 2

    LEVELS = ((FACTORY, "Завод"), (RETAILER, "Розничная сеть"), (SP, "Индивидуальный предприниматель"))

    product = models.ManyToManyField("products.Product", verbose_name="Товар", related_name="article")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец поставщика', **NULLABLE)

    name = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Номер дома')

    level = models.IntegerField(choices=LEVELS, default=FACTORY, verbose_name='Уровень')
    debt = models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('city',)
