from django.shortcuts import render

def mod_reportes (request):
    return render(request, 'modificar_reportes/modificar_report.html')

def vista_inventario(request):
    return render(request, 'inventario/inventario.html')

def vista_admin(request):
    return render(request, 'adminUsuarios/admin_user.html')  # Ruta al HTML de adminUsuarios

