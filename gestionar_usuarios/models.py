
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser




class Usuario(AbstractUser):
    TIPO_DOCUMENTO_CHOICES = [
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cédula de Ciudadanía'),
        ('RC', 'Registro Civil'),
        ('PA', 'Pasaporte'),
        ('CE', 'Cédula de Extranjería'),
    ]
    
    reset_token = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.CharField(max_length=150, unique=True)
    apellido = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES)
    documento = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    rol_de_usuario = models.CharField(max_length=50)
    correo = models.EmailField(max_length=254, unique=True)
    estado = models.BooleanField(default=True)

# Agregar `related_name` para evitar conflictos#
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario',
    )
# Create your models here.
