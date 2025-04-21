from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def listado_inventario(request):
    return render(request, 'inventario/inventario.html')
