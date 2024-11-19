from django.contrib import admin
from .models import Proveedor
from .models import Materiaprima

# Register your models here.

from django.contrib import admin
from .models import Proveedor, Materiaprima

# Define el administrador personalizado para Proveedor
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('idprovedor', 'nombreprovedor', 'direccion', 'telefono')  # Campos visibles en la tabla del admin

# Define el administrador personalizado para MateriaPrima
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('idmateriaprima', 'nombremateriaprima', 'costo', 'proveedor', 'cantidad', 
                    'unidadmedida', 'categoria', 'marca', 'fechallegada', 'fechavencimiento')  # Campos visibles

# Registra los modelos con sus respectivas clases Admin
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Materiaprima, MateriaPrimaAdmin)


'''
   search_fields = ('nombreMateriaPrima', 'categoria', 'marca')  # Habilita búsqueda por nombre, categoría y marca
    list_filter = ('categoria', 'marca', 'fechaLlegada')  # Filtros por categoría, marca y fecha de llegada
    ordering = ('nombreMateriaPrima',)  # Ordena por nombre
    list_editable = ('costo', 'cantidad')  # Permite editar costo y cantidad directamente en la lista
    list_per_page = 20  # Registros por página




    search_fields = ('nombreProvedor', 'direccion', 'telefono')  # Habilita búsqueda por nombre, dirección y teléfono
    list_filter = ('direccion',)  # Opcional: Filtros por dirección en la barra lateral
    ordering = ('nombreProvedor',)  # Ordena por nombre en la tabla
'''