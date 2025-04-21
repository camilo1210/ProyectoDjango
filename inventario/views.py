from django.shortcuts import render

def listado_inventario(request):
    return render(request, 'inventario/inventario.html')
