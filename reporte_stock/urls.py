from django.urls import path
from . import views
from . views import reporte_stock

urlpatterns = [
    path('', views.reporte_stock, name='reporte_stock'),
    path('api/productos/', views.api_productos, name='api_productos'),
    path("api/actualizar_producto/", views.actualizar_producto, name="actualizar_producto"),
    path('api/crear_producto/', views.crear_producto, name='crear_producto'),

]