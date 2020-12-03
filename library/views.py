from django.shortcuts import render, reverse
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, views, generics, status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .models import Book, Author, Category, EbookFile, Serie
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

class LibraryView(LoginRequiredMixin, TemplateView):
    template_name = 'library/library_home.html'
    login_url = '/account/login'

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return self.request.user.books.all()
    

class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    
    def get_queryset(self):
        return self.request.user.authors.all()

class UploadView(views.APIView):
    parser_class = (FileUploadParser)

    def get_queryset(self):
        return self.request.user.files.all()
    

    def post(self, request, format=None):
        
        print(request.FILES)
        
        for file in request.FILES:
            f = request.FILES[file]
            print(type(f))
            print(f.content_type)
            file_type = f.content_type
            ebook = EbookFile(file=f, book=Book.objects.get(pk=1), file_format=file_type, user=request.user)
            ebook.save()
        
        return Response(status=status.HTTP_201_CREATED)