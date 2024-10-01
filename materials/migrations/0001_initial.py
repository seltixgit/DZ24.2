# Generated by Django 4.2.2 on 2024-10-01 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название курса",
                        max_length=120,
                        verbose_name="Название куса",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Добавьте изображение",
                        null=True,
                        upload_to="materials/course/image",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Укажите описание курса",
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название урока",
                        max_length=150,
                        verbose_name="Урок",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Укажите описание урока",
                        null=True,
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Добавьте изображение",
                        null=True,
                        upload_to="materials/lesson/image",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "link_to_video",
                    models.CharField(
                        blank=True,
                        help_text="Укажите ссылку на видео",
                        max_length=150,
                        null=True,
                        verbose_name="Ссылка на видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите курс",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lesson",
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
