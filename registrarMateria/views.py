
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from .models import MateriaPrima


def vista_add_materia(request):
    return render(request, 'materia_prima/add_materia.html')

def agregar_materia(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombremateriapri')
        costo = request.POST.get('costo')
        proveedor = request.POST.get('proveedor')
        cantidad = request.POST.get('cantidad')
        unidad = request.POST.get('unidadmedida')
        categoria = request.POST.get('categoria')
        marca = request.POST.get('marca')
        fecha_llegada = parse_datetime(request.POST.get('fechallegada'))
        fecha_vencimiento = parse_datetime(request.POST.get('fechavencimiento'))

        materia = MateriaPrima(
            nombremateriapri=nombre,
            costo=costo,
            proveedor=proveedor,
            cantidad=cantidad,
            unidadmedida=unidad,
            categoria=categoria,
            marca=marca,
            fechallegada=fecha_llegada,
            fechavencimiento=fecha_vencimiento
        )
        materia.save()
        return redirect('agregar_materia')  # o redirige a una lista, como 'lista_materias'

    return render(request, 'agregar_materia.html')

