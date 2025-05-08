from django.urls import path, include
from rest_framework import routers
from books.models import *
from books.views import *





router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]

app_name = 'books'