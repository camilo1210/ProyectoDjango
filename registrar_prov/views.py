from django.shortcuts import render, redirect
from .forms import ProveedorForm
from django.contrib import messages

def registrar_prov(request):
    form = ProveedorForm()
    return render(request, 'registrar_prov/registrar_prov.html', {'form': form})

def registrar_proveedor(request):
    error = None
    try:
        if request.method == 'POST':
            form = ProveedorForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "¡Proveedor registrado con éxito!")
                return redirect('registrar_prov:registrar_prov')
            else:
                print("Errores en el formulario:", form.errors)
        else:
            form = ProveedorForm()
    except Exception as e:
        error = f"Ocurrió un error al registrar el proveedor: {str(e)}"
        print("Error durante el registro del proveedor:", error)
        form = ProveedorForm()

    return render(request, 'registrar_prov/registrar_prov.html', {
        'form': form,
        'error': error
    })
