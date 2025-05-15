from django.urls import path, include
from rest_framework import routers
from books.views import *


router = routers.DefaultRouter()
router.register("books", BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('books/', BookListView.as_view(), name='book-list'),
    # path('create/', BookCreateView.as_view(), name='book-create'),
    # path('update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
]

app_name = 'books'