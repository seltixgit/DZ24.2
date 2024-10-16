# Generated by Django 5.0.1 on 2024-10-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="link",
            field=models.URLField(
                blank=True,
                help_text="Укажите ссылку на оплату",
                max_length=400,
                null=True,
                verbose_name="Ссылка на оплату",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите id сессии",
                max_length=255,
                null=True,
                verbose_name="Id сессии",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateField(blank=True, null=True, verbose_name="Дата платежа"),
        ),
    ]
