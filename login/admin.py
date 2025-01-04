from .models import Materiaprima
from django.contrib import admin
from .models import LoginUsuario, Usuarios

admin.site.register(LoginUsuario)
admin.site.register(Usuarios)

