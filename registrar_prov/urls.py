from django.urls import path
from . import views

app_name = 'registrar_prov'

urlpatterns = [
    path('', views.registrar_prov, name='registrar_prov'),
    path('registrado/', views.registrar_proveedor, name='registrado'),
]
