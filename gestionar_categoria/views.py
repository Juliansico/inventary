from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import  Categoria
from .forms import  CategoriaForm

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def gestionar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestionar_categoria.html', {'categorias': categorias})



@login_required
def añadir_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría añadida con éxito.')
            return redirect('gestionar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'añadir_categoria.html', {'form': form})



@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada con éxito.')
            return redirect('gestionar_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})



@login_required
def activar_inactivar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.estado = not categoria.estado
    categoria.save()
    estado = "activada" if categoria.estado else "inactivada"
    messages.success(request, f'Categoría {estado} con éxito.')
    return redirect('gestionar_categoria')



@login_required
def consultar_categoria(request):
    if request.method == 'POST':
        id_categoria = request.POST.get('id_categoria')
        nombre = request.POST.get('nombre')
        categoria = None
        if id_categoria:
            categoria = Categoria.objects.filter(id=id_categoria).first()
        elif nombre:
            categoria = Categoria.objects.filter(nombre__icontains=nombre).first()
        if categoria:
            return render(request, 'consultar_categoria.html', {'categoria': categoria})
        else:
            messages.error(request, 'Categoría no encontrada.')
    return render(request, 'consultar_categoria.html')

@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria eliminada exitosamente.')
        return redirect('gestionar_categoria')  

    return render(request, 'confirmar_eliminacion_categoria.html', {'categoria': categoria})

