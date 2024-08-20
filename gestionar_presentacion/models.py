from django.db import models


class Presentacion(models.Model):
    nombre = models.CharField(max_length=255)
    precio_venta = models.FloatField()
    precio_compra = models.FloatField()
    cantidad_Stock = models.IntegerField()
    unidades_Paquete = models.IntegerField()
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
# Create your models here.
