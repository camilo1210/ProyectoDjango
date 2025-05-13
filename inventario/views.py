from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Materiaprima  

def listado_inventario(request):
    return render(request, 'inventario/inventario.html')

def configuracion(request):
    return render(request, 'configuracion/configuraciones.html')

def vista_add_materia(request):
    return render(request, 'materia_prima/add_materia.html')

def Inventario(request):
    materias = Materiaprima.objects.all()
    print(materias)
    return render(request, 'inventario/inventario.html', {'materias': materias})  # Ruta al HTML de Inventario
