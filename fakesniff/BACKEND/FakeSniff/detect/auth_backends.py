from django.contrib.auth.backends import BaseBackend
from .models import UserProfile
from django.contrib.auth.hashers import check_password

class UserProfileBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserProfile.objects.get(username=username)
            if check_password(password, user.password):
                return user
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None