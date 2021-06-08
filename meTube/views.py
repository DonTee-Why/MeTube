from django.shortcuts import render
from django.forms import ModelForm

from .models import AppUser, Video, Comment, Reply, Like
from django.forms.widgets import EmailInput, PasswordInput, TextInput

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
                'id': "first_name",
                'name': "first_name",
                'placeholder': "John"
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'id': "floatingSurname",
                'name': "floatingSurname",
                'placeholder': "John"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'id': "floatingEmail",
                'name': "floatingEmail",
                'placeholder': "John"
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'id': "floatingPassword",
                'name': "floatingPassword",
                'placeholder': "John"
            })
        }

# Create your views here.
def index(request):
    return render(request,"meTube/index.html", {
        "signInForm": SignInForm,
        "signUpForm": SignUpForm
    })