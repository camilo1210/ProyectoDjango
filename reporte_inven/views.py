from django.shortcuts import render

def reporte_inven (request):
    return render(request, 'reporte_inven/reporte_inven.html')