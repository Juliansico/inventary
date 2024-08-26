from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import CustomPasswordResetConfirmView
from .views import registrar


urlpatterns = [
    
    path('registrar/', registrar, name='registrar'),  # Verifica el nombre 'registrar'
    path('recuperar-contrasena/', auth_views.PasswordResetView.as_view(
        template_name='recuperar_contrasena.html',
        email_template_name='recuperar_contrasena_email.html',
        success_url=reverse_lazy('recuperar_contrasena_done')
    ), name='recuperar_contrasena'),
    path('recuperar-contrasena-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='recuperar_contrasena_done.html'
    ), name='recuperar_contrasena_done'),
    path('reset-password/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='restablecer_contrasena'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset_password_complete.html'
    ), name='reset_password_complete'),
]