# login/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout




# Create your views here.

def helloWork (request):
    return HttpResponse("hola mundo mi papa")

def about (request):
    return HttpResponse ("otro texto")



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal u otra página
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'login/login.html')

def home_view(request):
    return render(request, 'home/home.html')  # Actualiza la ruta si está dentro de 'home/'



def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión


