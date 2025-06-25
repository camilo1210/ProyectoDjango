from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.vista_add_materia, name='vista_add_materia'),
    path('materia-prima/agregar/', views.agregar_materia, name='agregar_materia'),
    path('registrar_prov/', views.registrar_prov, name='registrada_prov'),
    path('inventario/', views.vista_inventario, name='inventario'),
    
]
