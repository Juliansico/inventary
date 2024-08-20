from django.db import models

# Define tus modelos aquí.
class Compra(models.Model):
    fecha_Compra = models.DateTimeField()
    total_Compra = models.FloatField()
    cantidad_Producto = models.IntegerField()
    proveedor_Id = models.ForeignKey('gestionar_proveedor.Proveedor', on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    productos = models.ManyToManyField('gestionar_productos.Producto', through='Compra_has_producto')

class Compra_has_producto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey('gestionar_productos.Producto', on_delete=models.CASCADE)
