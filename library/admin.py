from django.contrib import admin

from .models import Author, Book, Serie, Category, EbookFile

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(EbookFile)
class EbookFileAdmin(admin.ModelAdmin):
    pass