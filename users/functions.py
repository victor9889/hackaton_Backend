from .models import UserData


def username_exists(username):
    return UserData.objects.filter(username=username).exists()