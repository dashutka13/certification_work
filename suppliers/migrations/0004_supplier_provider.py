# Generated by Django 5.1.1 on 2024-10-07 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0003_remove_supplier_provider"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplier",
            name="provider",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="suppliers.supplier",
                verbose_name="Поставщик",
            ),
        ),
    ]
