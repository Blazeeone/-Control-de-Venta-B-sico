from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

# READ (list)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/producto_list.html', {'object_list': productos})

# READ (detail)
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventario/producto_detail.html', {'object': producto})

# CREATE
@csrf_protect
def producto_create(request):
    """Vista protegida con CSRF"""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" creado exitosamente')
            return redirect('producto_list')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = ProductoForm()
    
    return render(request, 'inventario/producto_form.html', {'form': form})

# UPDATE
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance= producto)
        if form.is_valid():
            form.save()
            return redirect(producto_list)
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'inventario/producto_form.html', {'form': form})

# DELETE
def producto_delete(request, pk): 
    producto = get_object_or_404(Producto, pk=pk) 

    if request.method == 'POST': 
        producto.delete() 
        return redirect('producto_list') 
    
    return render(request, 'inventario/producto_confirm_delete.html', {'object': producto}) 