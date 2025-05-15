from django.db import models

import user
from books.models import Book


# Create your models here.
class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return = models.DateField()
    actual_return = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(user.models.User, on_delete=models.CASCADE, related_name='user')