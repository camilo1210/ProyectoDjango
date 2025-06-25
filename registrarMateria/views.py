from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from datetime import datetime
from .models import MateriaPrima
from registrar_prov.models import Proveedor

def agregar_materia(request):
    proveedores = Proveedor.objects.all()  # <--- Mover esta línea arriba

    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombreMateriaPrima')
            costo_str = request.POST.get('costo')
            proveedor_id_str = request.POST.get('proveedor')
            cantidad_str = request.POST.get('cantidad')
            unidad = request.POST.get('unidadMedida')
            categoria = request.POST.get('categoria')
            marca = request.POST.get('marca')
            fecha_llegada_str = request.POST.get('fechaLlegada')
            fecha_vencimiento_str = request.POST.get('fechaVencimiento')
            
            print("Valores recibidos:")
            print(f"costo: {costo_str}")
            print(f"proveedor: {proveedor_id_str}")
            print(f"cantidad: {cantidad_str}")

            
            

            if not all([costo_str, proveedor_id_str, cantidad_str]):
                print("❌ Error: Campos numéricos vacíos")
                return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})

            try:
                costo = int(costo_str)
                idProveedor = int(proveedor_id_str)
                cantidad = int(cantidad_str)
            except ValueError as ve:
                print("❌ Error convirtiendo números:", ve)
                return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})

            try:
                fecha_llegada = timezone.make_aware(
                    datetime.strptime(fecha_llegada_str, '%Y-%m-%dT%H:%M')
                )
                fecha_vencimiento = timezone.make_aware(
                    datetime.strptime(fecha_vencimiento_str, '%Y-%m-%dT%H:%M')
                )
            except ValueError as ve:
                print("❌ Error en formato de fecha:", ve)
                return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})

            try:
                proveedor = Proveedor.objects.get(idProvedor=idProveedor) 
            except Proveedor.DoesNotExist:
                print("❌ El proveedor no existe")
                return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})

            materia = MateriaPrima(
                nombreMateriaPrima=nombre,
                costo=costo,
                proveedor=proveedor,
                cantidad=cantidad,
                unidadMedida=unidad,
                categoria=categoria,
                marca=marca,
                fechaLlegada=fecha_llegada,
                fechaVencimiento=fecha_vencimiento
            )
            materia.save()
            print("✅ Guardado con éxito:", materia)
            return redirect('vista_add_materia')

        except Exception as e:
            print("❌ Error general:", e)
            return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})

    return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})


def vista_add_materia(request):
    proveedores = Proveedor.objects.all()
    print("Proveedores disponibles:", proveedores)  # Para debug
    return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})

def registrar_prov(request):
    return render(request, 'registrar_prov/registrar_prov.html')


    