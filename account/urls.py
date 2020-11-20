
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import forms
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.ProfileView.as_view(), name="profile"),
    path('login/', LoginView.as_view(template_name='account/login.html', form_class=forms.LoginForm), name='login'),
    path('lougout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]