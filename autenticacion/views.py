from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import FormularioRegistro, FormularioRecuperarContraseña, FormularioNuevaContraseña
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = FormularioRegistro()
    return render(request, 'registrar.html', {'formulario': formulario})

class RecuperarContraseñaView(PasswordResetView):
    template_name = 'recuperar_contrasena.html'
    email_template_name = 'recuperar_contrasena_email.html'
    subject_template_name = 'recuperar_contrasena_asunto.txt'
    success_url = reverse_lazy('password_reset_done')


class NuevaContraseñaView(PasswordResetConfirmView):
    form_class = FormularioNuevaContraseña
    template_name = 'nueva_contrasena.html'
    success_url = reverse_lazy('login')