from django.urls import include, path
from . import views


app_name = "meTube"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.sign_in_page, name="login"),
    path("signUp", views.signUp, name="signUp"),
    path("signIn", views.signIn, name="signIn"),
    path("signOut", views.signOut, name="signOut"),
    path("profile/<int:user_id>/", include([
        path("", views.profile, name="profile")
    ])),
    path("video/", include([
        path("add", views.add_video, name="add_video"),
        path("save", views.save_video, name="save_video"),
        path("<int:video_id>", views.watch_video, name="watch_video"),
        path("updateView", views.update_view, name="update_view")
    ]))
]
