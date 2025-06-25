"""
URL configuration for Sistema_invetario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),  # Incluye las rutas de la app 'login'
    path('', include('login.urls')),  # Incluye las rutas de la app 'login'
    path('adminUsuarios/', include('adminUsuarios.urls')),  # Incluye las rutas de la ap 'adminUsuarios'
    path('inventario/', include('inventario.urls')),  # Incluye las rutas de la app 'inventario'
    path('configuracion/', include('configuracion.urls')),  # Incluye las rutas de la app 'configuracion'
    path('modificar_reportes/', include('modificar_reportes.urls')),
    path('perfil/', include('perfil.urls')),
    path('proveedores/', include('registrar_prov.urls', namespace='registrar_prov')),
    path('registrar_salida/', include('registrar_salida.urls')),
    path('reporte_caduci/', include('reporte_caduci.urls')),
    path('reporte_compra/', include('reporte_compra.urls')),
    path('reporte_inven/', include('reporte_inven.urls')),
    path('reporte_provee/', include('reporte_provee.urls')),
    path('reporte_stock/', include('reporte_stock.urls')),
    path('reporte_tende/', include('reporte_tende.urls')),
    path('reporte_ventas/', include('reporte_ventas.urls')),
    path('materia/', include('registrarMateria.urls')),
    path('inventario/', include('inventario.urls', namespace='inventario')),
]