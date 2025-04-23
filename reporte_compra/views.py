from django.shortcuts import render

def reporte_compra (request):
    return render(request, 'reporte_compra/reporte_compra.html')
