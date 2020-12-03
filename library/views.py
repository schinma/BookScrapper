from django.shortcuts import render, reverse
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, views, generics, status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
import filetype

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
        
        if request.FILES['file']:
            f = request.FILES['file']
            type = filetype.guess(f)
            ebook = EbookFile(file=f, book=Book.objects.get(pk=1), file_format=type.extension, user=request.user)
            ebook.save()
            return Response(status=status.HTTP_201_CREATED)        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)