from rest_framework.viewsets import ModelViewSet
from books.serializers import *
from rest_framework import generics


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer