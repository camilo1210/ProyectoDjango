# login/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloWork),  # Ruta para helloWork
    path('about/', views.about),  # Ruta para about
    path('login/', views.login_view, name='login'),  # Ruta para el login
    path('home/', views.home_view, name='home'),  # Ruta para home
    path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesión
]

