from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Presentacion
from .forms import PresentacionForm


def dashboard(request):
    return render(request, 'dashboard.html')
@login_required

def gestionar_presentacion(request):
    presentaciones = Presentacion.objects.all()
    if request.method == 'POST':
        form = PresentacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presentación creada con éxito.')
            return redirect('gestionar_presentacion')
    else:
        form = PresentacionForm()
    return render(request, 'gestionar_presentacion.html', {'presentaciones': presentaciones, 'form': form})



@login_required
def añadir_presentacion(request):
    if request.method == 'POST':
        form = PresentacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presentación añadida con éxito.')
            return redirect('gestionar_presentacion')
    else:
        form = PresentacionForm()
    return render(request, 'añadir_presentacion.html', {'form': form})


@login_required
def editar_presentacion(request, presentacion_id):
    presentacion = get_object_or_404(Presentacion, id=presentacion_id)
    if request.method == 'POST':
        form = PresentacionForm(request.POST, instance=presentacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presentación actualizada con éxito.')
            return redirect('gestionar_presentacion')
    else:
        form = PresentacionForm(instance=presentacion)
    return render(request, 'editar_presentacion.html', {'form': form, 'presentacion': presentacion})



@login_required
def activar_inactivar_presentacion(request, presentacion_id):
    presentacion = get_object_or_404(Presentacion, id=presentacion_id)
    presentacion.estado = not presentacion.estado
    presentacion.save()
    estado = "activada" if presentacion.estado else "inactivada"
    messages.success(request, f'Presentación {estado} con éxito.')
    return redirect('gestionar_presentacion')



@login_required
def consultar_presentacion(request):
    if request.method == 'POST':
        id_presentacion = request.POST.get('id_presentacion')
        nombre = request.POST.get('nombre')
        presentacion = None
        if id_presentacion:
            presentacion = Presentacion.objects.filter(id=id_presentacion).first()
        elif nombre:
            presentacion = Presentacion.objects.filter(nombre__icontains=nombre).first()
        if presentacion:
            return render(request, 'consultar_presentacion.html', {'presentacion': presentacion})
        else:
            messages.error(request, 'Presentación no encontrada.')
    return render(request, 'consultar_presentacion.html')



@login_required
def eliminar_presentacion(request, presentacion_id):
    presentacion = get_object_or_404(Presentacion, id=presentacion_id)
    if request.method == 'POST':
        presentacion.delete()
        messages.success(request, 'Presentacion eliminada exitosamente.')
        return redirect('gestionar_presentacion')  

    return render(request, 'confirmar_eliminacion_presentacion.html', {'presentacion': presentacion})








# Create your views here.
