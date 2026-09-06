from django import forms
from .models import Producto

# Formulario para el modelo Producto para registrar y actualizar datos.
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto  
        # Actualizar campos 
        fields = ['codigo', 'nombre', 'precio', 'stock']