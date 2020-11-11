from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, Author, Category, EbookFile, Serie

# Create your views here.

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = ''