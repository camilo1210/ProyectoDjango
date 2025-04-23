from django.urls import path
from . import views
from . views import reporte_inven

urlpatterns = [
    path('', views.reporte_inven, name='reporte_inven'),
]