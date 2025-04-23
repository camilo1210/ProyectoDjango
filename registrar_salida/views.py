from django.shortcuts import render

def registrar_salida (request):
    return render(request, 'registrar_salida/registrar_salida.html')