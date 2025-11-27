from django.db import models
from .habitacion import Habitacion
from .huesped import Huesped

class Venta_Habitacion(models.Model):
    TIPO_ESTADIA = (
        ('dos_horas', 'Dos Horas'),
        ('estadia', 'Estadía'),
    )
    METODO_PAGO = (
        ('efectivo', 'efectivo'),
        ('transferencia', 'transferencia'),
    )
    huesped = models.ForeignKey(Huesped, on_delete=models.SET_NULL, null=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.SET_NULL, null=True)
    fecha_entrada = models.DateTimeField(auto_now_add=True)  
    fecha_salida = models.DateTimeField(null=True, blank=True)  
    precio_pagado = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO, default='efectivo')
    tipo_estadia = models.CharField(max_length=20, choices=TIPO_ESTADIA, default='estadia')
    extras = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return f"{self.huesped} - {self.habitacion} - {self.fecha_entrada} - {self.fecha_salida} - {self.precio_pagado} - {self.metodo_pago}"

    class Meta:
        verbose_name = 'Venta Habitacion'
        verbose_name_plural = 'Ventas Habitaciones'


    def save(self, *args, **kwargs):
        if self.tipo_estadia == 'dos_horas':
            self.precio_pagado = self.habitacion.obtener_precio_dos_horas() + self.extras or 0
        else:
            self.precio_pagado = self.habitacion.precio + self.extras or 0
        super().save(*args, **kwargs)