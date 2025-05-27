from django.shortcuts import render
from .models import Proveedor  # Asegúrate del nombre correcto del modelo
from django.http import JsonResponse

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