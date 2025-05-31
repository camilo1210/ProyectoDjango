from django.shortcuts import render
from django.http import JsonResponse
from inventario.models import Materiaprima
from collections import defaultdict
def reporte_caduci (request):
    return render(request, 'reporte_caduci/reporte_caduci.html')

def materias_por_fecha_json(request):
    materias = Materiaprima.objects.all().values(
        'nombremateriaprima', 'categoria', 'marca', 'cantidad', 'unidadmedida', 'fechavencimiento'
    )
    
    agrupadas = defaultdict(list)
    for materia in materias:
        fecha = materia['fechavencimiento'].date().isoformat()  # YYYY-MM-DD
        agrupadas[fecha].append({
            'nombre': materia['nombremateriaprima'],
            'categoria': materia['categoria'],
            'marca': materia['marca'],
            'cantidad': materia['cantidad'],
            'unidad': materia['unidadmedida'],
        })

    return JsonResponse(agrupadas)
