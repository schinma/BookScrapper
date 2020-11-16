from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'bio', 'website']

class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=False)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author')