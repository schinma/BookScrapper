from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    serie = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)