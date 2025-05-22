from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.settings import api_settings

from books.permissions import IsAdminOrReadOnly
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LoginUserView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class =  UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

class ManageUserView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
