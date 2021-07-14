from django.contrib.auth import *
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
import os
from django.utils import timezone

def video_upload_path(instance, filename):
    return 'videos/user_{0}/{1}'.format(instance.user.id, filename)
class AppUser(models.Model):

    

    class Meta:
        verbose_name = _("AppUser")
        verbose_name_plural = _("AppUsers")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("AppUser_detail", kwargs={"pk": self.pk})

    first_name = models.CharField(_("First Name"), max_length=256)
    surname = models.CharField(_("Surname"), max_length=256)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    password = models.CharField(_("Password"), max_length=256)
    avatar = models.ImageField(_("Avatar"), upload_to='avatar/', height_field=500, width_field=500, max_length=None, blank=True)
    last_login = models.DateTimeField(_('Last Login'), blank=True, null=True)
    date_created = models.DateTimeField(_("Date Created"), auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(_("Date Modified"), auto_now=True, auto_now_add=False)
    
    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

class Video(models.Model):

    

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Video_detail", kwargs={"pk": self.pk})

    title = models.CharField(_("Tile"), max_length=50)
    caption = models.CharField(_("Caption"), max_length=256)
    user = models.ForeignKey("AppUser", verbose_name=_("User"), on_delete=models.CASCADE)
    video = models.FileField(_("Video"), upload_to=video_upload_path, max_length=100)
    active = models.BooleanField(_("Active"), default=True)
    date_added = models.DateTimeField(_("Date Added"), auto_now=False, auto_now_add=True)

class Like(models.Model):

    

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Like_detail", kwargs={"pk": self.pk})

    user = models.ForeignKey("AppUser", verbose_name=_("User"), on_delete=models.CASCADE)
    video = models.ForeignKey("Video", verbose_name=_("Video"), on_delete=models.CASCADE)
    date = models.DateTimeField(_("Date Added"), auto_now=False, default=timezone.now)

class Comment(models.Model):

    

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})

    user = models.ForeignKey("AppUser", verbose_name=_("User"), on_delete=models.CASCADE)
    comment = models.CharField(_("Comment"), max_length=256)
    video = models.ForeignKey("Video", verbose_name=_("Video"), on_delete=models.CASCADE)
    date = models.DateTimeField(_("Date Added"), auto_now=False, default=timezone.now)

class Reply(models.Model):

    

    class Meta:
        verbose_name = _("Reply")
        verbose_name_plural = _("Replies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Reply_detail", kwargs={"pk": self.pk})

    user = models.ForeignKey("AppUser", verbose_name=_("User"), on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", verbose_name=_("Comment"), on_delete=models.CASCADE)
    date = models.DateTimeField(_("Date Added"), auto_now=False, default=timezone.now)

class View(models.Model):

    

    class Meta:
        verbose_name = _("View")
        verbose_name_plural = _("Views")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("View_detail", kwargs={"pk": self.pk})

    user = models.ForeignKey("AppUser", verbose_name=_("User"), on_delete=models.CASCADE)
    video = models.ForeignKey("Video", verbose_name=_("Video"), on_delete=models.CASCADE)
    date = models.DateTimeField(_("Date Added"), auto_now=False, auto_now_add=True)
