from django.contrib import admin
from .models import Materiaprima


# Register your models here.

class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('idMateriaPrima', 'nombreMateriaPrima', 'costo', 'cantidad', 'unidadMedida', 'categoria', 'marca', 'fechaLlegada', 'fechaVencimiento')
    search_fields = ('nombreMateriaPrima', 'categoria', 'marca')
    list_filter = ('categoria', 'marca', 'unidadMedida')

admin.site.register(Materiaprima)