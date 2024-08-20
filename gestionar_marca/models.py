from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    logoTipo = models.ImageField(upload_to='logoTipo/', blank=True, null=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
