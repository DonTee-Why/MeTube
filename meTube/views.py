from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import AppUser, Video, Comment, Reply, Like
from .forms import *
from django.contrib.auth.hashers import make_password


forms = {
    "signInForm": SignInForm,
    "signUpForm": SignUpForm
    }
    
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "meTube/login.html", forms)
    else:
        videos = Video.objects.all()
        return render(request, "meTube/index.html", {
            "videos":videos
            })

def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return render(request, "meTube/login.html", {
                "sign_up_status": "ok",
                "forms": forms
            })
    return render(request, "meTube/login.html", {
        "status": "error",
        "forms": forms
    })
    
def signIn(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect(reverse('meTube:profile', args=[request.user.id]))
        else:
            return render(request, "meTube/login.html", {
                "sign_in_status": "error",
                "forms": forms
            })
    return render(request, "meTube/login.html", {
        "sign_in_status": "error",
        "forms": forms
    })
    
def signOut(request):
    logout(request)
    return render(request, "meTube/login.html", {
        "sign_out_status": "ok",
        "forms": forms
    })
    
def profile(request, user_id):
    user = AppUser.objects.get(pk=user_id)
    videos = Video.objects.filter(user=user_id)
    
    return render(request, "meTube/profile/index.html", {
        "user": user,
        "videos": videos
    })
