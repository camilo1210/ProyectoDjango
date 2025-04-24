from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.vista_add_materia, name='agregar_materia'),
    path('materia-prima/agregar/', views.agregar_materia, name='agregar_materia'),
    
]
