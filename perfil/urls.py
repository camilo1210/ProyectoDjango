from django.urls import path
from . import views
from . views import perfil

urlpatterns = [
    path('', views.perfil, name='perfil'),
]
