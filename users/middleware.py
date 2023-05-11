from django.shortcuts import redirect
from django.contrib import messages

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_routes = ['/','/login/','/register/', '/admin/']

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in self.public_routes:
            messages.error(request, 'Para acceder a esta página debe iniciar sesión')
            return redirect('login')
        response = self.get_response(request)
        return response