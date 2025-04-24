from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def listado_inventario(request):
    return render(request, 'inventario/inventario.html')

def configuracion(request):
    return render(request, 'configuracion/configuraciones.html')

def vista_add_materia(request):
    return render(request, 'materia_prima/add_materia.html')