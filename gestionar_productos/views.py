from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
import logging

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def gestionar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestionar_productos.html', {'productos': productos})


@login_required
def añadir_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto añadido con éxito.')
            return redirect('gestionar_productos')
    else:
        form = ProductoForm()
    return render(request, 'añadir_producto.html', {'form': form})


@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito.')
            return redirect('gestionar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})


@login_required
def consultar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        producto = Producto.objects.filter(nombre__icontains=nombre).first()
        return render(request, 'consultar_productos.html', {'producto': producto})
    return render(request, 'gestionar_productos.html')


@login_required
def activar_inactivar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.estado = not producto.estado
    producto.save()
    estado = "activado" if producto.estado else "inactivado"
    messages.success(request, f'Producto {estado} con éxito.')
    return redirect('gestionar_productos')


