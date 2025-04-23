from django.urls import path
from . import views
from .views import configuracion_home
urlpatterns = [
    path('', views.configuracion_home, name='configuracion'),
]
