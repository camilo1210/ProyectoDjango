from django.urls import path
from . import views
from . views import registrar_prov

urlpatterns = [
    path('', views.registrar_prov, name='registrar_prov'),
]