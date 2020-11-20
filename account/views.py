from django.shortcuts import render
from django.views.generic import DetailView
from .models import CustomUser

# Create your views here.

class ProfileView(DetailView):
    
    model = CustomUser
    template_name = 'account/account.html'

    def get_object(self):
        return self.request.user