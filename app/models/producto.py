from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    cantidad = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre + " - " + str(self.precio) + " - " + str(self.cantidad)
    
    def tiene_stock(self):
        return  self.cantidad > 0