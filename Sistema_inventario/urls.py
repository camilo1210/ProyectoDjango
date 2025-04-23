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
    path('adminUsuarios/', include('adminUsuarios.urls')),  # Incluye las rutas de la ap  'adminUsuarios'
    path('inventario/', include('inventario.urls')),  # Incluye las rutas de la app 'inventario'
    path('configuracion/', include('configuracion.urls')),  # Incluye las rutas de la app 'configuracion'
    path('modificar_reportes/', include('modificar_reportes.urls')),

]
