from rest_framework import serializers
from books.models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =("id", "title", "author", "cover", "inventory", "daily_fee")

class BookListSerializer(BookSerializer):
    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields

class BookCreateSerializer(BookSerializer):
    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields


class BookRetrieveSerializers(BookSerializer):
    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields



