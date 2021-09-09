from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import AppUser, Video, Comment, Reply, Like
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


forms = {
    "signInForm": SignInForm,
    "signUpForm": SignUpForm
    }

# Create your views here.
@login_required
def index(request):
    videos = Video.objects.all()
    return render(request, "meTube/index.html", {
        "videos":videos
        })

def sign_in_page(request):
    return render(request, "meTube/login.html", {"forms": forms})

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
    return redirect(reverse('meTube:login'))
    
def signIn(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect(reverse('meTube:index'))
        else:
            return render(request, "meTube/login.html", {
                "sign_in_status": "error",
                "forms": forms
            })
    return redirect(reverse('meTube:login'))
    
@login_required
def signOut(request):
    logout(request)
    return render(request, "meTube/login.html", {
        "sign_out_status": "ok",
        "forms": forms
    })
    
@login_required
def profile(request, user_id):
    user = AppUser.objects.get(pk=user_id)
    videos = Video.objects.filter(user=user)
    return render(request, "meTube/profile/index.html", {
        "user": user,
        "videos": videos
    })
    
@login_required
def add_video(request):
    return render(request, "meTube/video/index.html", {
        "videoUploadForm": VideoUploadForm
    })
    
@login_required
def save_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            caption = form.cleaned_data['caption']
            video = form.cleaned_data['video']
            user = AppUser.objects.get(pk=int(request.user.id))
            video = Video(title=title, caption=caption, user=user, video=video)
            video.save()
            return redirect(reverse('meTube:profile', args=[request.user.id]))
    else:
        return render(request, "meTube/video/index.html", {
            "status": "error",
            "videoUploadForm": VideoUploadForm
        })

@login_required
def watch_video(request, video_id):
    video = Video.objects.get(pk=video_id)
    user = AppUser.objects.get(pk=video.user_id)
    return render(request, "meTube/video/watch.html",{
        "video": video,
        "user": user
    })
