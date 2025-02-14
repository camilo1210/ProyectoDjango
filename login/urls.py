# login/urls.py
from django.urls import path# type: ignore
from . import views
from login.views import loginRegister, home 
from adminUsuarios.views import admin
from django.contrib.auth.views import LogoutView #el manejo de logout usando el Django # type: ignore
from adminUsuarios.views import admin

urlpatterns = [
    path('', views.loginRegister, name='login'),  # Ruta para login
    path('admin/', admin , name='admin'),
    path('', loginRegister, name='login'),
    path('home/', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),# Redirige al inicio después de cerrar sesión

    
]

