from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Borrowing
from .serializers import BorrowingSerializer, BorrowingListSerializer, BorrowingDetailSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BorrowingListSerializer
        elif self.action == 'retrieve':
            return BorrowingDetailSerializer
        else:
            return BorrowingSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.inventory < 1:
            raise serializers.ValidationError("This book is not available")
        book.inventory -= 1
        book.save()

        serializer.save()