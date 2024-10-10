from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(
        max_length=120, verbose_name="Название куса", help_text="Укажите название курса"
    )
    image = models.ImageField(
        upload_to="materials/course/image",
        **NULLABLE,
        verbose_name="Изображение",
        help_text="Добавьте изображение",
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание курса", help_text="Укажите описание курса"
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец курса",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Урок", help_text="Укажите название урока"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Курс",
        help_text="Выберите курс",
        related_name="lesson",
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание урока", help_text="Укажите описание урока"
    )
    image = models.ImageField(
        upload_to="materials/lesson/image",
        **NULLABLE,
        verbose_name="Изображение",
        help_text="Добавьте изображение",
    )
    link_to_video = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец урока",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
