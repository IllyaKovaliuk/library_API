from datetime import datetime, date

from rest_framework import serializers

from books.models import Book
from books.serializers import BookSerializer
from user.serializers import UserSerializer
from .models import Borrowing


book = BookSerializer(read_only=True)
user = UserSerializer(read_only=True)


class BorrowingSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()
    book_name = serializers.CharField(source='book.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Borrowing
        fields = ("id", "borrow_date","expected_return", "actual_return", "book", "book_name", "user", "username", "is_active")

    def get_is_active(self, obj):
        return obj.actual_return is None or obj.actual_return > date.today()


class BorrowingListSerializer(BorrowingSerializer):
    class Meta:
        model = Borrowing
        fields = ("id", "borrow_date", "book_name", "is_active")


class BorrowingDetailSerializer(BorrowingSerializer):
    class Meta:
        model = Borrowing
        fields = ("id", "borrow_date", "expected_return", "actual_return","book_name", "username", "is_active")