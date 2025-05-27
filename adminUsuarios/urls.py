# login/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.admin, name='adminUsuarios'),  # Ruta principal para adminUsuarios
    path('api/usernames/', views.get_usernames, name='get_usernames'),
    path('api/delete-user/', views.delete_user, name='delete-user'),
    path('api/update-user/', views.update_user, name='update-user'),
    
]

