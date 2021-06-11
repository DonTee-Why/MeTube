from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import AppUser

class MeTubeBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = AppUser.objects.get(email=email)
            password_valid = check_password(password, user.password)
            if password_valid:
                return user
        except AppUser.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            return AppUser.objects.get(pk=user_id)
        except AppUser.DoesNotExist:
            return None