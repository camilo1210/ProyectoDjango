from django.shortcuts import render
from .models import Proveedor  # Asegúrate del nombre correcto del modelo
from django.http import JsonResponse
from .models import MateriaPrima

def reporte_provee (request):
    return render(request, 'reporte_provee/reporte_provee.html')
def obtener_proveedores(request):
    proveedores = Proveedor.objects.all()
    print("Cantidad de proveedores:", proveedores.count())  # Esto debe salir en consola

    data = [
        {
            "id": p.idProvedor,
            "nombre": p.nombreProvedor,
            "direccion": p.direccion,
            "telefono": p.telefono,
        }
        for p in proveedores
    ]

    return JsonResponse(data, safe=False)
def materias_por_proveedor(request, proveedor_id):
    materias = MateriaPrima.objects.filter(proveedor=proveedor_id)
    data = [
        {
            "id": m.idMateriaPrima,
            "nombre": m.nombreMateriaPrima,
            "costo": m.costo,
            "cantidad": m.cantidad,
            "unidadMedida": m.unidadMedida,
            "categoria": m.categoria,
            "marca": m.marca,
            "fechaLlegada": m.fechaLlegada.strftime("%Y-%m-%d"),
            "fechaVencimiento": m.fechaVencimiento.strftime("%Y-%m-%d"),
        }
        for m in materias
    ]
    return JsonResponse(data, safe=False)