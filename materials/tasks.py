from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

from users.models import User


@shared_task
def sample_task():
    print("Task is running...")
    sleep(10)
    print("Task finished")

@shared_task
def send_course_update_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )


@shared_task
def deactivate_inactive_users():

    one_month_ago = timezone.now() - timedelta(days=30)

    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)


    inactive_users.update(is_active=False)

    return f'Deactivated {inactive_users.count()} users'