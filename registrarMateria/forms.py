# inventario/forms.py
from django import forms
from .models import MateriaPrima

class MateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = '__all__'  
