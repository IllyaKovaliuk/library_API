from django.shortcuts import render
from django.utils.datetime_safe import datetime
from rest_framework import viewsets, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from notifications.tasks import send_reminder, send_notification
from notifications.telegram import send_reminder_telegram

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
        today = datetime.today()
        borrowing = serializer.save(user=self.request.user)
        book = serializer.save(user=self.request.user)

        notification_message = (f"You have created new borrowing\n"
                                f"You borrowing ID = '{borrowing.pk}'\n"
                                f"You take book '{borrowing.book.title}'\n"
                                f"Your username '{borrowing.user.username}'\n"
                                f"Return it before {borrowing.expected_return} please"
                                )


        send_notification(notification_message)

        reminder_text = (f"You must return book with id = {borrowing.book.pk}\n"
                         f"{borrowing.expected_return}\n"
                         f"Today is {today}\n"
                         f"Your paid fee will be raised every day\n"
                         f"Thanks for your understanding!\n"
        )

        send_reminder(reminder_text)
