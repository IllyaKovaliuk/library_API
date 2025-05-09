from django.db import models

import user
from books.models import Book


# Create your models here.
class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return = models.DateField()
    actual_return = models.DateField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user.models.User, on_delete=models.CASCADE, related_name='user')