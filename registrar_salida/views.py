from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Salida  # Asegúrate de tener importado tu modelo Salida
import json
def registrar_salida (request):
    return render(request, 'registrar_salida/registrar_salida.html')
def api_productos(request):
    productos = Producto.objects.all()
    data = [
        {   
            'id_producto': p.id_producto,
            'nombre': p.nombre,
            'categoria': p.categoria,
            'precio': float(p.precio),
            'cantidad': p.cantidad
        }
        for p in productos
    ]
    return JsonResponse(data, safe=False)
@csrf_exempt
def guardar_salida(request):
    if request.method == "POST":
        try:
            datos = json.loads(request.body)
            productos = datos.get("productos")
            cantidades = datos.get("cantidad")  # ← corregido aquí

            print("Datos recibidos en la vista:")
            print(f"Productos: {productos}")
            print(f"Cantidad: {cantidades}")

            if not productos or not cantidades:
                return JsonResponse({"error": "Faltan datos"}, status=400)
            print(f"Creando salida con: fecha={timezone.now()}, productos={productos}, cantidad={cantidades}")

            salida = Salida.objects.create(
                fecha=timezone.now(),
                productos=productos,
                cantidad=cantidades,
                materias_primas=""
            )

            return JsonResponse({"mensaje": "Salida guardada exitosamente"})
        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)
