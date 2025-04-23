from django.shortcuts import render

def reporte_provee (request):
    return render(request, 'reporte_provee/reporte_provee.html')
