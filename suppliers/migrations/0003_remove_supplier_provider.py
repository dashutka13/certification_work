# Generated by Django 5.1.1 on 2024-10-07 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0002_supplier_provider"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supplier",
            name="provider",
        ),
    ]
