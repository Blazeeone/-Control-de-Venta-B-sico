from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages # Importado para evitar errores de ejecución
from .models import Producto, Cliente
from .forms import ProductoForm

# READ (list): Mostrar listado de productos disponibles
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/producto_list.html', {'object_list': productos})

# READ (detail): Ver detalle de un producto
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'ventas/producto_detail.html', {'object': producto})

# CREATE: Registrar el producto a vender con nombre, código, cantidad y precio
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
    
    return render(request, 'ventas/producto_form.html', {'form': form})

# UPDATE: Permitir actualizar stock y otros datos del producto
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list') # Corregido: añadido comillas para evitar error de ejecución
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'ventas/producto_form.html', {'form': form})

# DELETE: Permitir eliminar productos
def producto_delete(request, pk): 
    producto = get_object_or_404(Producto, pk=pk) 

    if request.method == 'POST': 
        producto.delete() 
        return redirect('producto_list') 
    
    return render(request, 'ventas/producto_confirm_delete.html', {'object': producto}) 

# VENTA (Caso 2): Registrar venta, actualizar stock y manejar cliente
@csrf_protect
def registrar_venta(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        rut_cliente = request.POST.get('rut')
        es_habitual = request.POST.get('es_habitual') == 'on'
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        cantidad_vender = int(request.POST.get('cantidad', 1))
        
        # Validar datos de entrada y actualizar stock
        if cantidad_vender <= producto.stock:
            producto.stock -= cantidad_vender
            producto.save()
            
            # Estructura de decisión para cliente habitual o boleta ocasional
            if es_habitual:
                cliente, created = Cliente.objects.get_or_create(rut=rut_cliente)
                cliente.habitual = True
                cliente.nombre = nombre
                cliente.telefono = telefono
                cliente.save()
            else:
                cliente, created = Cliente.objects.get_or_create(rut=rut_cliente)
                cliente.habitual = False
                cliente.save()
                
            messages.success(request, 'Venta registrada con éxito. Stock actualizado.')
            return redirect('producto_list')
        else:
            messages.error(request, 'No hay stock suficiente.')
            
    return render(request, 'ventas/registrar_venta.html', {'producto': producto})