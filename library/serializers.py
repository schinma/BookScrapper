from rest_framework import serializers

from .models import Book, Author


class AuhtorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class BookSerializer(serializers.ModelSerializer):

    author = AuhtorSerializer(many=False)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author')