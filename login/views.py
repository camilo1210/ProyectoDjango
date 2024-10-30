# login/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario




# Create your views here.

def loginRegister(request):
    if request.method == 'POST':
        if 'name' in request.POST:  # Para el registro
            nombre = request.POST['name']
            email = request.POST['email']
            contraseña = request.POST['password']
            
            nuevo_usuario = Usuario(nombre=nombre, email=email, contraseña=contraseña)
            nuevo_usuario.save()
            
            messages.success(request, 'Registro exitoso.')
            return redirect('loginRegister')  # Redirigir a la misma vista

        elif 'username' in request.POST:  # Para el inicio de sesión
            username = request.POST['username']
            password = request.POST['password']
            # Aquí iría la lógica de autenticación
            
    return render(request, 'login/login.html')  # Asegúrate de que la ruta sea correcta
