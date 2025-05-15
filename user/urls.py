from django.urls import path, include
from rest_framework import routers
from .models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CreateUserView, UpdateUserView, ManageUserView

urlpatterns = [
    path('/register/', CreateUserView.as_view(), name='register'),
    path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('/update/', UpdateUserView.as_view(), name='update'),
    path('/me/', ManageUserView.as_view(), name='me'),
]

app_name = 'user'