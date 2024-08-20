from django.db import models
from django.conf import settings
from gestionar_productos.models import Producto


class Venta(models.Model):
    nombre_Producto = models.CharField(max_length=255)
    precio_Producto = models.FloatField()
    cantidad_Venta = models.FloatField()
    total_Venta_Realizada = models.FloatField(editable=False)  # Cambiado a editable=False
    estado = models.BooleanField(default=True)
    saldo_Inicial = models.FloatField(null=True, blank=True)  # Permitir nulo
    saldo_Actual = models.FloatField(null=True, blank=True)  # Permitir nulo
    fecha_Apertura = models.DateTimeField()
    fecha_Cierre = models.DateTimeField(null=True, blank=True)  # Permitir nulo
    id_Usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='Ventas_has_producto')

    def save(self, *args, **kwargs):
        self.total_Venta_Realizada = self.precio_Producto * self.cantidad_Venta
        super().save(*args, **kwargs)

class Ventas_has_producto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
# Create your models here.
