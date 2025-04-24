
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from .models import MateriaPrima
from registrar_prov.models import Proveedores


def vista_add_materia(request):
    return render(request, 'materia_prima/add_materia.html')


def agregar_materia(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreMateriaPrima')
        costo = request.POST.get('costo')
        proveedor_id = request.POST.get('proveedor')  # De aquí obtienes el ID
        cantidad = request.POST.get('cantidad')
        unidad = request.POST.get('unidadMedida')
        categoria = request.POST.get('categoria')
        marca = request.POST.get('marca')
        fecha_llegada = parse_datetime(request.POST.get('fechaLlegada'))
        fecha_vencimiento = parse_datetime(request.POST.get('fechaVencimiento'))

        try:
            proveedor = Proveedores.objects.get(idProvedor=int(proveedor_id))  # Obtener instancia

            materia = MateriaPrima(
                nombreMateriaPrima=nombre,
                costo=int(costo),
                proveedor=proveedor,  # Pasas el objeto, no el ID
                cantidad=int(cantidad),
                unidadMedida=unidad,
                categoria=categoria,
                marca=marca,
                fechaLlegada=fecha_llegada,
                fechaVencimiento=fecha_vencimiento
            )      
            materia.save()
            print("✅ Guardado con éxito:", materia)
            return redirect('agregar_materia')

        except Proveedores.DoesNotExist:
            print("❌ El proveedor no existe.")
        except Exception as e:
            print("❌ Error al guardar:", e)

    return render(request, 'materia_prima/add_materia.html')
