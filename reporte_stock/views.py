from django.shortcuts import render

def reporte_stock (request):
    return render(request, 'reporte_stock/reporte_stock.html')

