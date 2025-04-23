from django.shortcuts import render

def mod_reportes (request):
    return render(request, 'modificar_reportes/modificar_report.html')