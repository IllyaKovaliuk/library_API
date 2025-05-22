from datetime import date

from celery import Celery, shared_task
from django.utils import timezone

from borrowing.models import Borrowing
from notifications.telegram import send_message
from notifications.telegram import send_reminder_telegram


app = Celery('tasks', broker='redis://localhost',backend='redis://localhost')

@shared_task
def send_notification(message):
    send_message(message)


@shared_task
def send_reminder(reminder):
    send_reminder_telegram(reminder)