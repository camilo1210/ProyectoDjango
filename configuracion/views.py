from django.shortcuts import render

def configuracion_home (request):
    return render(request, 'configuracion/configuraciones.html')
