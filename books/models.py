from django.db import models

import user
from user.models import User

class Book(models.Model):
    class StatusCover(models.TextChoices):
        HARD = 'Hard'
        SOFT = 'Soft'


    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.CharField(max_length=100, choices=StatusCover.choices)
    inventory = models.IntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)
