from django.urls import path
from . import views
from . views import reporte_tende

urlpatterns = [
    path('', views.reporte_tende, name='reporte_tende'),
    path("productos_mas_fabricados/", views.productos_mas_fabricados, name="productos_mas_fabricados"),

]