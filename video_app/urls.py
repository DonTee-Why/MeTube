from django.urls import path
from . import views

app_name = "video_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("signIn", views.sign_in, name="signIn")
]