from django.urls import path
from . import views

app_name = "meTube"
urlpatterns = [
    path("", views.index, name="index"),
    path("signUp", views.signUp, name="signUp"),
    path("signIn", views.signIn, name="signIn"),
]
