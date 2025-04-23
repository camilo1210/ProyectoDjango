from django.urls import path
from . import views
from . views import reporte_provee

urlpatterns = [
    path('', views.reporte_provee, name='reporte_provee'),
]