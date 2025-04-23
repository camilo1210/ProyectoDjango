from django.urls import path
from . import views
from . views import reporte_compra

urlpatterns = [
    path('', views.reporte_compra, name='reporte_compra'),
]