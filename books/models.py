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


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return = models.DateField()
    actual_return = models.DateField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user.models.User, on_delete=models.CASCADE, related_name='user')