from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import listado_inventario

app_name = 'inventario'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listado_inventario, name='home'),
]
