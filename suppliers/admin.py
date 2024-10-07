from django.contrib import admin
from suppliers.models import Supplier


@admin.action(description="Очистить задолженность перед поставщиком")
def debt_zero(modeladmin, request, queryset):
    queryset.update(debt=0)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'level', 'debt',)
    list_filter = ('city',)
    actions = [debt_zero]
