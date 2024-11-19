# login/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .models import Usuarios




# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import LoginUsuario
from django.contrib.auth.models import User 
from .models import Usuarios

def loginRegister(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'sign-in':  # Manejo de inicio de sesión
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin/')  # Redirigir al admin después de iniciar sesión
            else:
                messages.error(request, "Credenciales incorrectas.")
        
        elif request.POST.get('action') == 'sign-up':  # Manejo de registro
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if not User.objects.filter(username=name).exists():  # Evita duplicados
                user = User.objects.create_user(username=name, email=email, password=password)
                user.is_staff = True
                user.is_superuser = True  # Otorga permisos completos
                user.save()
                messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
                return redirect('login')  # Redirigir al login después del registro
            else:
                messages.error(request, "Este nombre de usuario ya está registrado.")
    return render(request, 'login/login.html')
'''
def register(request):
    # Lógica de registro
    return render(request, 'login/register.html')
'''