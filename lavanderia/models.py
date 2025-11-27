from django.db import models
from habitaciones.models import Huesped
class Orden_Lavanderia(models.Model):
    ESTADOS = [
        ('en_espera', 'En espera'),
        ('lavado', 'Lavado'),
    ]
    huesped = models.ForeignKey(Huesped, on_delete=models.SET_NULL, null=True)
    cantidad_prendas = models.PositiveIntegerField()  
    valor_por_prenda = models.DecimalField(max_digits=10, decimal_places=0, default=3000)  
    valor_total = models.DecimalField(max_digits=10, decimal_places=0)  
    fecha_orden = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='en_espera')

    class Meta:
        verbose_name = 'Orden Lavanderia'
        verbose_name_plural = 'Ordenes Lavanderia'

    def __str__(self):
        return f"Orden de lavandería para {self.huesped.primer_nombre} {self.huesped.primer_apellido} ({self.cantidad_prendas} prendas) - {self.valor_total} - {self.estado}"

    def save(self, *args, **kwargs):
        self.valor_total = self.cantidad_prendas * self.valor_por_prenda
        super().save(*args, **kwargs)
