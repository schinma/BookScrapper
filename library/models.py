from django.db import models
from django.conf import settings

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authors') 
        
    class Meta:
        ordering = ['last_name', 'first_name']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
 
    def __str__(self):
        return self.full_name()


class Serie(models.Model):
    title = models.CharField(max_length=100)
    ordering_title = models.CharField(max_length=100, default='', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='series')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='series')
    
    class Meta:
        ordering = ['title', 'author']
 
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    ordering_title = models.CharField(max_length=100, default='', blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    serie = models.ForeignKey(Serie, on_delete=models.PROTECT, related_name='books', blank=True, null=True)
    serie_number = models.SmallIntegerField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    read = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    date_read = models.DateField(blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)
    synopsis = models.TextField(blank=True, default='')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')
    
    class Meta:
        ordering = ['date_added', 'ordering_title', 'title', 'author']
 
    def __str__(self):
        return self.title

class EbookFile(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='files')
    file = models.FileField()
    file_format = models.CharField(max_length=20)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.file.name
