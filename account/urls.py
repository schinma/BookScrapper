
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import forms

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html', form_class=forms.LoginForm), name='login'),
    path('lougout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]