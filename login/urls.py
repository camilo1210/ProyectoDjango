# login/urls.py
from django.urls import path
from . import views
from .views import loginRegister

urlpatterns = [
    path('', views.loginRegister, name='loginRegister'),  # Ruta para loginRegister
    
]

