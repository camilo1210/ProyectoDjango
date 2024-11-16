# login/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminUsuarios, name='Administracion Usuarios'),  # Ruta para la administracion 
    
]

