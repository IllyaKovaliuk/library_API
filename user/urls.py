from django.urls import path, include
from rest_framework import routers
from .models import User

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]

app_name = 'user'