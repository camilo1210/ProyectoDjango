from django.urls import path
from . import views
from . views import registrar_salida

urlpatterns = [
    path('', views.registrar_salida, name='registrar_salida'),
    path("api/productos/", views.api_productos, name="api_productos"),
    path('guardar/', views.guardar_salida, name='guardar_salida'),

]