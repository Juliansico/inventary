from django.urls import path
from . import views
from .views import registrar, RecuperarContraseñaView, NuevaContraseñaView
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('recuperar_contrasena/', RecuperarContraseñaView.as_view(), name='recuperar_contrasena'),
    path('recuperar_contrasena/done/', TemplateView.as_view(template_name='recuperar_contrasena_done.html'), name='recuperar_contrasena_done'),
    path('recuperar_contrasena/<uidb64>/<token>/', NuevaContraseñaView.as_view(), name='password_reset_confirm'),
]