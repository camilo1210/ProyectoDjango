# login/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.admin, name='admin'),  # Ruta principal para adminUsuarios
    
]

