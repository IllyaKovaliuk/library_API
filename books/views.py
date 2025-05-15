from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from books.permissions import IsAuthenticatedOrReadOnly, IsAdminOrReadOnly
from books.serializers import *
from rest_framework import generics
from rest_framework import viewsets



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        elif self.action == 'retrieve':
            return BookRetrieveSerializers
        return BookSerializer

#
# class BookListView(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer

#
# class BookCreateView(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookCreateSerializer

#
# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookUpdateSerializer