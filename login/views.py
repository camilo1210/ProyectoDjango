# login/views.py

from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from login.models import LoginUsuario  # Modelo personalizado
from django.contrib.auth.models import User  # Modelo de Django

def loginRegister(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        # Manejo de inicio de sesión
        if action == 'sign-in':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Verificar el rol en el campo first_name
                if user.first_name == 'Admin':
                    login(request, user)
                    return redirect('/adminUsuarios/')  # Redirigir al admin
                elif user.first_name == 'Usuario':
                    login(request, user)
                    return redirect('/home/')  # Redirigir al home del usuario
                else:
                    messages.error(request, 'El usuario no tiene un rol válido asignado.')
            else:
                messages.error(request, "Credenciales incorrectas.")

        # Manejo de registro
        elif action == 'sign-up':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Verificar si el usuario ya existe
            if not User.objects.filter(username=name).exists():
                # Crear usuario en el sistema de autenticación de Django
                user = User.objects.create_user(username=name, email=email, password=password, first_name='Usuario')
                user.save()

                # (Opcional) Crear usuario en el modelo LoginUsuario si es necesario
                nuevo_usuario = LoginUsuario(usuario=name, email=email, contraseña=password)
                nuevo_usuario.save()

                messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
                return redirect('login')  # Redirigir al login
            else:
                messages.error(request, "Este nombre de usuario ya está registrado.")

    return render(request, 'login/login.html')


'''
def register(request):
    # Lógica de registro
    return render(request, 'login/register.html')
'''

def adminUsuarios(request):
    return render(request, 'adminUsuarios/admin_user.html')  # Ruta al HTML de adminUsuarios

def home(request):
    return render(request, 'inventario/inventario.html')  # Ruta al HTML de home
