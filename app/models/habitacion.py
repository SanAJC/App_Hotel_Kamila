from django.db import models

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
        estado = 'Disponible' if self.disponible else 'No Disponible'
        aire = 'Aire' if self.tiene_aire else 'Ventilador'
        return f"Habitacion {self.numero} - ({aire}) - Valor: {self.precio} - ( {estado} )"

    def obtener_precio_dos_horas(self):
        return 45000 if self.tiene_aire else 35000

