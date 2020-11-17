from django.urls import path
from rest_framework import routers

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('api/books/', views.BookViewSet.as_view({'get' : 'list'}), name='book-list'),
]