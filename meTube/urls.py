from django.urls import include, path
from . import views


app_name = "meTube"
urlpatterns = [
    path("", views.index, name="index"),
    path("signUp", views.signUp, name="signUp"),
    path("signIn", views.signIn, name="signIn"),
    path("signOut", views.signOut, name="signOut"),
    path("profile/<int:user_id>", include([
        path("", views.profile, name="profile")
    ]))
]
