from django.urls import path
from rest_framework import routers

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.LibraryView.as_view(), name='books'),
    path('api/books/', views.BookListView.as_view(), name='book-list'),
    #path('api/books/<int:pk>', views.BookViewSet.as_view({'get' : 'retrieve'}), name='book-detail'),
    path('api/authors/<int:pk>', views.AuthorView.as_view({'get' : 'retrieve'}), name='author-detail'),
    path('api/upload', views.UploadView.as_view(), name="upload"),
]