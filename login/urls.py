# login/urls.py
from django.urls import path# type: ignore
from . import views
from login.views import loginRegister 
from adminUsuarios.views import admin
from django.contrib.auth.views import LogoutView #el manejo de logout usando el Django # type: ignore
from adminUsuarios.views import admin

urlpatterns = [
    path('', views.loginRegister, name='login'),  # Ruta para login
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),


]

