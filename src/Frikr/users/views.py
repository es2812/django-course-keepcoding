from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm

def login(request):
    error_msg = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form.get('usr')
        password = form.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_msg.append('Nombre de usuario o contraseña incorrectos')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('photos_home')
            else:
                error_msg.append('Usuario no activo')
    else:
        form = LoginForm()
    context = {
        "login_form": form,
        "errors": error_msg
    }
    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('photos_home')