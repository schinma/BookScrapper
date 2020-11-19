from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row
from crispy_forms.bootstrap import Alert

from .models import CustomUser


class LoginForm(AuthenticationForm):
    """
    Custom Login form with crispy-form form helper
    """

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('account:login')        
        self.helper.add_input(Submit('submit', 'Connexion', css_class="offset-md-10"))      
        self.helper.wrapper_class = 'row justify-content-center'
        self.helper.label_class = 'col-md-3 col-form-label'
        self.helper.field_class = 'col-md-6'


class CustomUserCreationForm(UserCreationForm):
    """
    Custom User Creation Form to go with the custom user model
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
    
class CustomUserChangeForm(UserChangeForm):
    """
    Custom User Change Form to go with the custom user model
    """

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('library:books')
        self.helper.form_id = 'edit-form'
        self.helper.add_input(Submit('submit', 'Enregistrer'))
        self.helper.layout = Layout(
            Field('username', type='hidden'),
            Field('email', ),
            Alert(
                content="L'adresse email n'est pas valide", 
                css_class="alert-danger d-none", 
                css_id="email-error",
                ),
        )      

    class Meta :
        model = CustomUser
        fields = ('username', 'email')
        labels = {
            "email" : "Addresse email",
        }
