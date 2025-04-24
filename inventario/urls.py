# inventario/urls.py
from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.listado_inventario, name='home'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('agregar/', views.vista_add_materia, name='agregar_materia'),  # ← usa la que ya tienes
]
