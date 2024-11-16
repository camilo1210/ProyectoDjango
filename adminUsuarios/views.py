from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .models import Usuario

# Create your views here.

from django.shortcuts import render
from .models import Usuario  # Importa el modelo Usuario

def admin(request):
    
    if request.method == 'POST':
        if request.POST.get('action') == 'sign-in':  # Manejo de inicio de sesión
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir a la página de inicio después de iniciar sesión
            else:
                messages.error(request, "Credenciales incorrectas.")
    
