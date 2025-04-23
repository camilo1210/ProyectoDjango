from django.urls import path
from . import views
from . views import reporte_ventas

urlpatterns = [
    path('', views.reporte_ventas, name='reporte_ventas'),
]