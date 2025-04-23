from django.shortcuts import render

def vista_add_materia(request):
    return render(request, 'materia_prima/add_materia.html')
