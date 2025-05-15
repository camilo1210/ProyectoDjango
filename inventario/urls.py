# inventario/urls.py
from django.urls import path
from . import views

app_name = 'inventario_app'

urlpatterns = [
    path('', views.Inventario, name='Inventario'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('agregar/', views.vista_add_materia, name='agregar_materia'),
    path('eliminar/<int:idmateriaprima>/', views.eliminar_materia, name='delete_materia'),
    path('actualizar/<int:id>/', views.actualizar_materia, name='actualizar_materia'),

]
