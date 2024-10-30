# login/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginRegister),  # Ruta para loginRegister
    
]

