from django.db import models
from habitaciones.models import Huesped
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


class Venta_Producto(models.Model):
    METODO_PAGO = (
        ('efectivo', 'efectivo'),
        ('transferencia', 'transferencia'),
    )
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    huesped = models.ForeignKey(Huesped, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)
    precio_pagado = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO, default='efectivo')
    fecha_venta = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Venta Producto'
        verbose_name_plural = 'Ventas Productos'

    def __str__(self):
        return f"{self.producto} - {self.cantidad} - {self.precio_pagado} - {self.metodo_pago} - {self.fecha_venta}"
    
    def save(self, *args, **kwargs):
        if self.cantidad > self.producto.cantidad:
            raise ValueError("No hay suficiente stock para esta venta.")
        self.precio_pagado = self.producto.precio * self.cantidad
        self.producto.cantidad -= self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)
