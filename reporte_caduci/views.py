from django.shortcuts import render

def reporte_caduci (request):
    return render(request, 'reporte_caduci/reporte_caduci.html')