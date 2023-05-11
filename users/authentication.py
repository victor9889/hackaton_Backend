from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import UserData

class UserDataBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_data = UserData.objects.get(username=username)
            if user_data.check_password(password):
                try:
                    user = User.objects.get(username=user_data.username)
                except User.DoesNotExist:
                    # Create a new Django user account if one doesn't exist
                    user = User.objects.create_user(username=user_data.username, email=user_data.username, password=password)
                return user
        except UserData.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
 