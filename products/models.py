from django.db import models
from django.utils import timezone
from users.models import User
from suppliers.models import Supplier
from config.settings import NULLABLE


class Product(models.Model):
    """Модель товара."""
    name = models.CharField(max_length=150, verbose_name="Название товара")
    model = models.CharField(max_length=150, verbose_name="Модель товара")
    date_release = models.DateTimeField(verbose_name="Дата выхода на рынок", default=timezone.now)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, **NULLABLE)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик', related_name="provider" ,**NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.model}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['-date_release']
