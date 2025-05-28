
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from datetime import datetime
from .models import MateriaPrima
from registrar_prov.models import Proveedores

def agregar_materia(request):
    if request.method == 'POST':
        try:
            # Obtener y validar datos
            nombre = request.POST.get('nombreMateriaPrima')
            costo_str = request.POST.get('costo')
            proveedor_id_str = request.POST.get('proveedor')
            cantidad_str = request.POST.get('cantidad')
            unidad = request.POST.get('unidadMedida')
            categoria = request.POST.get('categoria')
            marca = request.POST.get('marca')
            fecha_llegada_str = request.POST.get('fechaLlegada')
            fecha_vencimiento_str = request.POST.get('fechaVencimiento')

            # Verificar que los campos numéricos no sean None
            if not all([costo_str, proveedor_id_str, cantidad_str]):
                print("❌ Error: Campos numéricos vacíos")
                print(f"costo: {costo_str}")
                print(f"proveedor_id: {proveedor_id_str}")
                print(f"cantidad: {cantidad_str}")
                return render(request, 'materia_prima/add_materia.html')

            # Convertir strings a números
            try:
                costo = int(costo_str)
                proveedor_id = int(proveedor_id_str)
                cantidad = int(cantidad_str)
            except ValueError as ve:
                print("❌ Error convirtiendo números:", ve)
                return render(request, 'materia_prima/add_materia.html')

            # Convertir fechas
            try:
                fecha_llegada = timezone.make_aware(
                    datetime.strptime(fecha_llegada_str, '%Y-%m-%dT%H:%M')
                )
                fecha_vencimiento = timezone.make_aware(
                    datetime.strptime(fecha_vencimiento_str, '%Y-%m-%dT%H:%M')
                )
            except ValueError as ve:
                print("❌ Error en formato de fecha:", ve)
                return render(request, 'materia_prima/add_materia.html')

            # Obtener proveedor
            try:
                proveedor = Proveedores.objects.get(pk=proveedor_id)
            except Proveedores.DoesNotExist:
                print("❌ El proveedor no existe")
                return render(request, 'materia_prima/add_materia.html')

            # Crear y guardar materia prima
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
            return render(request, 'materia_prima/add_materia.html')

    return render(request, 'materia_prima/add_materia.html')


def vista_add_materia(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'materia_prima/add_materia.html', {'proveedores': proveedores})

def registrar_prov(request):
    return render(request, 'registrar_prov/registrar_prov.html')
    