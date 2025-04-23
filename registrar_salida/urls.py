from django.urls import path
from . import views
from . views import registrar_salida

urlpatterns = [
    path('', views.registrar_salida, name='registrar_salida'),
]