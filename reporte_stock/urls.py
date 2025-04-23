from django.urls import path
from . import views
from . views import reporte_stock

urlpatterns = [
    path('', views.reporte_stock, name='reporte_stock'),
]