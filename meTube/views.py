from django.shortcuts import *
from django.forms import *
from django.http import *
from django.urls import *
from django.contrib.auth import authenticate, login, logout

from .models import AppUser, Video, Comment, Reply, Like
from django.contrib.auth.hashers import make_password

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
    if not request.user.is_authenticated:
        return render(request,"meTube/index.html", {
            "signInForm": SignInForm,
            "signUpForm": SignUpForm
        })
    else:
        return render(request, "meTube/index.html")
    
def signIn(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email = email, password = password)
        if user:
            return redirect(reverse('meTube:profile'))
        else:
            return render(request, "meTube/index.html", {
                "sign_in_status": "error",
                "signInForm": SignInForm,
                "signUpForm": SignUpForm
            })
    return render(request, "meTube/index.html", {
        "sign_in_status": "error",
        "signInForm": SignInForm,
        "signUpForm": SignUpForm
    })