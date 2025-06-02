from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
@require_POST
def actualizar_producto(request):
    try:
        data = json.loads(request.body)

        producto_id = data.get("id")
        nuevo_precio = data.get("precio")
        nueva_cantidad = data.get("cantidad")


        producto = Producto.objects.get(id_producto=producto_id)

        # Validaciones (opcional)
        if nuevo_precio is None or nueva_cantidad is None:
            return JsonResponse({"success": False, "error": "Faltan datos"}, status=400)

        producto.precio = nuevo_precio
        producto.cantidad = nueva_cantidad
        producto.save()

        return JsonResponse({"success": True, "mensaje": "Producto actualizado correctamente."})

    except Producto.DoesNotExist:
        return JsonResponse({"success": False, "error": "Producto no encontrado."}, status=404)
    except Exception as e:
        print("Error:", str(e))  # 👈 Te muestra la excepción real en la terminal
        return JsonResponse({"success": False, "error": str(e)}, status=400)

    try:
        data = json.loads(request.body)

        nombre = data.get("nombre")
        categoria = data.get("categoria")
        precio = data.get("precio")
        cantidad = data.get("cantidad")

        producto = Producto.objects.create(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            cantidad=cantidad,
        )

        return JsonResponse({"success": True, "id": producto.id_producto})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=400)

@csrf_exempt  # Solo si no usas token CSRF
@require_POST
def crear_producto(request):
    try:
        datos = json.loads(request.body)

        nombre = datos.get("nombre")
        categoria = datos.get("categoria")
        precio = datos.get("precio")
        cantidad = datos.get("cantidad")

        producto_nuevo = Producto.objects.create(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            cantidad=cantidad
        )

        return JsonResponse({"exito": True, "mensaje": "Producto registrado correctamente."})

    except Exception as error:
        return JsonResponse({"exito": False, "mensaje": str(error)}, status=400)

