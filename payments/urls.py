from django.urls import path, include
from rest_framework import routers
from .models import Payment


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]

app_name = 'payments'