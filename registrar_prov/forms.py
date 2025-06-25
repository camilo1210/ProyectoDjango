# forms.py
from django import forms
from .models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['nombreProvedor', 'direccion', 'telefono']
        widgets = {
            'nombreProvedor': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            }
