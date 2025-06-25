import traceback 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Materiaprima  
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import Materiaprima
from .models import Proveedor
from datetime import datetime
from django.db import connection, transaction
from django.utils.timezone import make_aware
from django.db import reset_queries, connection
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware
from datetime import datetime
def listado_inventario(request):
    return render(request, 'inventario/inventario.html')

def configuracion(request):
    return render(request, 'configuracion/configuraciones.html')

def vista_add_materia(request):
    return render(request, 'materia_prima/add_materia.html')

def Inventario(request):
    materias = Materiaprima.objects.all()
    return render(request, 'inventario/inventario.html', {'materias': materias})  # Ruta al HTML de Inventario
def eliminar_materia(request, idmateriaprima):
    materia = get_object_or_404(Materiaprima, pk=idmateriaprima)
    materia.delete()
    return redirect('inventario:Inventario')

@csrf_exempt
def actualizar_materia(request,id):
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body)
            print("\n--- DATOS RECIBIDOS ---")
            print(data)
            materia = Materiaprima.objects.get(pk=id)
            materia.nombremateriaprima = data['nombremateriaprima']
            materia.costo = data['costo']
            materia.cantidad = data['cantidad']
            materia.unidadmedida = data['unidadmedida']
            materia.categoria = data['categoria']
            materia.marca = data['marca']
            materia.fechallegada = data['fechallegada']
            materia.fechavencimiento = data['fechavencimiento']
            # Manejo de proveedor: se debe convertir el ID en una instancia del modelo Proveedor
            proveedor_id = data.get('proveedor')

            print ("soy la badera----------------------------------------------------------------------")
            if proveedor_id:
                try:
                    proveedor = Proveedor.objects.get(pk=proveedor_id)
                    materia.proveedor = proveedor
                    print("Proveedor asignado correctamente")

                except Proveedor.DoesNotExist:
                    print("Proveedor no encontrado")
                    return JsonResponse({'success': False, 'error': 'Proveedor no encontrado'}, status=400)

            try:
                reset_queries()
                materia.save()
            except Exception as e:
                print(">>> ERROR:", e)

            print("Materia actualizada correctamente.")
            return JsonResponse({'success': True})

        except Exception as e:
            print("\n--- ERROR DETECTADO ---")
            traceback.print_exc()  # Muestra el error completo en consola
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)
@csrf_exempt
def inspeccionar_tabla_materiaprima(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DESCRIBE materiaprima")
            resultado = cursor.fetchall()
            columnas = [
                {
                    'Field': fila[0],
                    'Type': fila[1],
                    'Null': fila[2],
                    'Key': fila[3],
                    'Default': fila[4],
                    'Extra': fila[5]
                }
                for fila in resultado
            ]
        return JsonResponse({'estructura': columnas})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)