from django.urls import path
from . import views
from . views import mod_reportes
urlpatterns = [
    path('', views.mod_reportes, name='modificar_reportes' ),
    path('inventario/', views.vista_inventario, name='inventario'),
    path('modificar_reportes/', mod_reportes, name='modificar_reportes' ),
    path('adminUsuarios/', views.vista_admin, name='admin'),
]