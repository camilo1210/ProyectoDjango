# login/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout




# Create your views here.

def loginRegister(request):

    return render (request, 'login/login.html') #Dirige a la plantilla login.html
    if request.method == 'POST':
        if 'sign-in' in request.POST:  # Manejo de inicio de sesión
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir a la página de inicio después de iniciar sesión
            else:
                messages.error(request, "Credenciales incorrectas.")
        
        elif 'sign-up' in request.POST:  # Manejo de registro
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username=email, password=password, first_name=name)
            user.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')  # Redirigir al login después del registro

from django.shortcuts import render

def register(request):
    # Lógica de registro
    return render(request, 'login/login.html')
