from django.shortcuts import render, redirect
from .forms import ProveedorForm
from django.contrib import messages

def registrar_prov(request):
    form = ProveedorForm()
    return render(request, 'registrar_prov/registrar_prov.html')
    

def registrar_proveedor(request):
    error = None
    try:
        if request.method == 'POST':
            form = ProveedorForm(request.POST)
            print("Datos recibidos del formulario:", form.data)
            if form.is_valid():
                form.save()
                messages.success(request, "¡Proveedor registrado con éxito!")
                #return redirect('registrarMateria:agregar_materia')  # <- esto es clave
                return redirect('registrar_prov:registrar_prov')
            else:
                print("Errores en el formulario:", form.errors)  # Imprime los errores del formulario en la consola
        else:
            form = ProveedorForm()
    except Exception as e:
        error = f"Ocurrió un error al registrar el proveedor: {str(e)}"
        print("Error durante el registro del proveedor:", error)  # Imprime el error si ocurre
        form = ProveedorForm()

    return render(request, 'registrar_prov/registrar_prov.html', {
        'form': form,
        'error': error
    })
    
    

