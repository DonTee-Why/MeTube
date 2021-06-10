from django.shortcuts import *
from django.forms import *

from .models import AppUser, Video, Comment, Reply, Like

class SignInForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ['email', 'password']
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
                'id': "floatingEmail",
                'name': "floatingEmail",
                'placeholder': "Email Address"
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'id': "floatingPassword",
                'name': "floatingPassword",
                'placeholder': "Password"
            })
        }

class SignUpForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ['first_name','surname', 'email', 'password']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'id': "floatingFirstName",
                'name': "floatingFirstName",
                'placeholder': "John"
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'id': "floatingSurname",
                'name': "floatingSurname",
                'placeholder': "Doe"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'id': "floatingEmail",
                'name': "floatingEmail",
                'placeholder': "Email Address"
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'id': "floatingPassword",
                'name': "floatingPassword",
                'placeholder': "Password"
            })
        }

# Create your views here.
def index(request):
    return render(request,"meTube/index.html", {
        "signInForm": SignInForm,
        "signUpForm": SignUpForm
    })