from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


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


class Payment(models.Model):
    PAYMENT_METHODS = [("cash", "Наличные"), ("transfer", "Перевод на счет")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Session ID", help_text="Session ID")
    link = models.URLField(max_length=400, blank=True, null=True, verbose_name="Payment")


    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Payment by {self.user.email} on {self.payment_date}"