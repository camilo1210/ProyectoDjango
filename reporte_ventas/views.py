from django.shortcuts import render

def reporte_ventas (request):
    return render(request, 'reporte_ventas/reporte_ventas.html')
