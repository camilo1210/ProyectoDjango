# login/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginRegister, name='login'),  # Ruta para login
    path('register/', views.register, name='register'),  # Nueva ruta para register
]



