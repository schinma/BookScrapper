from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets

from .models import Book, Author, Category, EbookFile, Serie
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'library/library_home.html'


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()