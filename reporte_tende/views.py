from django.shortcuts import render

def reporte_tende (request):
    return render(request, 'reporte_tende/reporte_tende.html')
from django.shortcuts import render
from registrar_salida.models import Salida
from reporte_tende.models import Producto
from collections import defaultdict
from django.http import JsonResponse

def productos_mas_fabricados(request):
    contador = defaultdict(int)

    # Recorremos todas las salidas
    for salida in Salida.objects.all():
        ids = salida.productos.split(",")
        cantidades = salida.cantidad.split(",")

        for i in range(len(ids)):
            try:
                id_producto = int(ids[i])
                cantidad = int(cantidades[i])
                contador[id_producto] += cantidad
            except (ValueError, IndexError):
                continue  # ignoramos errores si algún valor no es válido

    # Creamos una lista con los productos y su cantidad total fabricada
    productos_fabricados = []
    for id_producto, total_fabricado in contador.items():
        try:
            producto = Producto.objects.get(pk=id_producto)
            productos_fabricados.append({
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "precio": float(producto.precio),
                "stock": producto.cantidad,
                "total_fabricado": total_fabricado
            })
        except Producto.DoesNotExist:
            continue

    # Ordenamos de mayor a menor según cantidad fabricada
    productos_fabricados.sort(key=lambda x: x["total_fabricado"], reverse=True)

    return JsonResponse({"productos": productos_fabricados})

