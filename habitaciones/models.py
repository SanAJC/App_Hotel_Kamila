from django.db import models

class Huesped(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15 , unique=True)
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Huesped'
        verbose_name_plural = 'Huespedes'

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"

class Habitacion(models.Model):
    numero = models.CharField(max_length=10 , unique=True)
    tiene_aire = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    disponible = models.BooleanField(default=True)
    cantidad_personas = models.IntegerField(default=2)

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        estado = 'Disponible' if self.disponible else 'Ocupada'
        aire = 'Aire' if self.tiene_aire else 'Ventilador'
        return f"Habitacion {self.numero} - ({aire}) - Valor: {self.precio} - ( {estado} )"

    def obtener_precio_dos_horas(self):
        return 45000 if self.tiene_aire else 35000


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
    precio_pagado = models.DecimalField(max_digits=10, decimal_places=0, null=True , blank=True)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO, default='efectivo')
    tipo_estadia = models.CharField(max_length=20, choices=TIPO_ESTADIA, default='estadia')
    extras = models.DecimalField(max_digits=10, decimal_places=0, null=True , blank=True)

    def __str__(self):
        return f"{self.huesped} - {self.habitacion} - {self.fecha_entrada} - {self.fecha_salida} - {self.precio_pagado} - {self.metodo_pago}"

    class Meta:
        verbose_name = 'Venta Habitacion'
        verbose_name_plural = 'Ventas Habitaciones'


    def save(self, *args, **kwargs):
        if self.tipo_estadia == 'dos_horas':
            self.precio_pagado = self.habitacion.obtener_precio_dos_horas() + self.extras or 0
            self.habitacion.disponible = False
            self.habitacion.save()
        else:
            self.precio_pagado = self.habitacion.precio + self.extras or 0
            self.habitacion.disponible = False
            self.habitacion.save()
        super().save(*args, **kwargs)
