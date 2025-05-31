from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto

def reporte_stock (request):
    return render(request, 'reporte_stock/reporte_stock.html')

def api_productos(request):
    productos = Producto.objects.all()
    data = [
        {
            'id': p.id_producto,
            'nombre': p.nombre,
            'categoria': p.categoria,
            'precio': float(p.precio),
            'cantidad': p.cantidad
        }
        for p in productos
    ]
    return JsonResponse(data, safe=False)