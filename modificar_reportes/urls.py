from django.urls import path
from . import views
from . views import mod_reportes
urlpatterns = [
    path('', views.mod_reportes, name='modificar_reportes' ),
]