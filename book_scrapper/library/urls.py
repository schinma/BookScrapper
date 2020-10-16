from django.urls import path

from . import views

urlpatterns = [
    path('api/library', views.BookListCreate.as_view(), name="create"),
]