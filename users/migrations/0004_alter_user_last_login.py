# Generated by Django 5.0.1 on 2024-10-17 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payment_link_payment_session_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime.now,
                null=True,
                verbose_name="Время последнего посещения",
            ),
        ),
    ]
