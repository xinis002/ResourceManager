from django.conf import settings
from django.db import models

import users


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание курса", help_text="Опишите курс"
    )
    photo = models.ImageField(
        upload_to="materials/photo",
        verbose_name="Фото",
        help_text="Загрузите фотографию курса",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="owner",
        help_text="Укажите владельца урока",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Урок", help_text="Укажите название урока"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание урока", help_text="Опишите урок"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберите курс",
        null=True,
        blank=True,
        related_name="lessons",
    )
    photo = models.ImageField(
        upload_to="materials/photo",
        verbose_name="Фото",
        help_text="Загрузите фотографию урока",
        blank=True,
        null=True,
    )
    video = models.URLField(
        blank=True, null=True, verbose_name="Видео", help_text="Загрузите видео урока"
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="owner",
        help_text="Укажите владельца урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"



class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f'{self.user} subscribed to {self.course}'