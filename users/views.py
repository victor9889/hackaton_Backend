from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserData
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .functions import  username_exists

@require_http_methods(["GET"])
def index(request):
    return render(request, 'users/index.html')

@require_http_methods(["POST", "GET"])
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else    :
            messages.error(request, 'El nombre de usuario o la contraseña son incorrectos')
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')

@require_http_methods(["POST", "GET"])
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username_exists(username):
            messages.error(request, 'El nombre de usuario ya existe.')
            return render(request, 'users/register.html')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = UserData(username=username, password=password)
        User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
    return render(request, 'users/register.html')

@require_http_methods(["POST", "GET"])
def home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'users/home.html')
