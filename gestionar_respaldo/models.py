
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Respaldo(models.Model):
    nombre_archivo = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tamano = models.FloatField()

    def _str_(self):
        return self.nombre_archivo