from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

def login(request):
    error_msg = []
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_msg.append('Nombre de usuario o contraseña incorrectos')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('photos_home')
            else:
                error_msg.append('Usuario no activo')
    context = {
        "errors": error_msg
    }
    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('photos_home')