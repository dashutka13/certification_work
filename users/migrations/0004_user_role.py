# Generated by Django 5.1.1 on 2024-10-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options_user_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("admin", "админ"), ("user", "пользователь")],
                default="user",
                verbose_name="Роль пользователя",
            ),
        ),
    ]
