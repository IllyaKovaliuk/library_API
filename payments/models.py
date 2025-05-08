from django.db import models

import books
from books.models import Borrowing


# Create your models here.
class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        PAID = 'Paid'


    class TypeChoices(models.TextChoices):
        PAYMENT = 'Payment'
        FINE = 'Fine'


    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    type = models.CharField(max_length=20, choices=TypeChoices.choices)
    borrowing_id = models.ForeignKey(books.models.Borrowing, on_delete=models.CASCADE)
    session_url = models.URLField() # url to stripe payment session
    session_id = models.CharField(max_length=50) # id of stripe payment session
    money_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

