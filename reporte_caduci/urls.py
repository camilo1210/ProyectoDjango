from django.urls import path
from . import views
from . views import reporte_caduci

urlpatterns = [
    path('', views.reporte_caduci, name='reporte_caduci'),
]