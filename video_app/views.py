from django import forms
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "video_app/index.html")

def sign_in(request):
    
    return NotImplemented()