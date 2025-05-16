from django import forms
from .models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['nombreProvedor', 'direccion', 'telefono']
