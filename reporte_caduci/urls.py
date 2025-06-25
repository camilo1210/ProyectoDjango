from django.urls import path
from . import views
from . views import reporte_caduci

urlpatterns = [
    path('', views.reporte_caduci, name='reporte_caduci'),
    path('api/data/', views.materias_por_fecha_json, name='caduci_data'),

]