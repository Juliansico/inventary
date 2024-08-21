from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm

def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def gestionar_usuarios(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(
            Q(usuario__icontains=query) |
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(documento__icontains=query)
        )
    else:
        usuarios = Usuario.objects.all()
    
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'gestionar_usuarios.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def añadir_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password1'])
            usuario.save()
            messages.success(request, 'Usuario añadido con éxito.')
            return redirect('gestionar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'añadir_usuario.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            if form.cleaned_data['password1']:
                usuario.set_password(form.cleaned_data['password1'])
            usuario.save()
            messages.success(request, 'Usuario actualizado con éxito.')
            return redirect('gestionar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def activar_inactivar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.estado = not usuario.estado
    usuario.save()
    estado = "activado" if usuario.estado else "inactivado"
    messages.success(request, f'Usuario {estado} con éxito.')
    return redirect('gestionar_usuarios')




@login_required
@user_passes_test(lambda u: u.is_superuser)
def consultar_usuario(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        usuario = Usuario.objects.filter(documento=documento).first()
        if usuario:
            return render(request, 'consultar_usuario.html', {'usuario': usuario})
        else:
            messages.error(request, 'Usuario no encontrado.')
    return render(request, 'consultar_usuario.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('gestionar_usuarios')  

    return render(request, 'confirmar_eliminacion_usuario.html', {'usuario': usuario})

