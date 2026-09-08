from django import forms
from django.core.exceptions import ValidationError
from .models import Producto

# Formulario para el modelo Producto para registrar y actualizar datos.
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto  
        fields = ['codigo', 'nombre', 'precio', 'stock']
        # Limita los campos en el HTML para evitar valores negativos
        widgets = {
            'precio': forms.NumberInput(attrs={'min': '1'}),
            'stock': forms.NumberInput(attrs={'min': '0'})
        }

    # Valida mediante estructuras de decisión que el precio sea mayor a 0
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise ValidationError("El precio debe ser estrictamente mayor a 0.")
        return precio

    # Valida que el stock no sea negativo (permite 0 por si el producto se agota)
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise ValidationError("El stock no puede ser un valor negativo.")
        return stock