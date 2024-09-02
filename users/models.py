from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Enter a valid email address"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone",
        blank=True,
        null=True,
        help_text="Enter phone number in format +7-XXX-XXX-XXXX",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="City",
        blank=True,
        null=True,
        help_text="Enter city name",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Avatar",
        blank=True,
        null=True,
        help_text="Upload user avatar",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = " Пользователь"
        verbose_name_plural = "Пользователи"
