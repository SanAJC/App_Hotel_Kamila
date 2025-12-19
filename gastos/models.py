from django.db import models

# Create your models here.

class Gasto(models.Model):
    METODO_PAGO = (
        ('efectivo', 'efectivo'),
        ('transferencia', 'transferencia'),
    )
    fecha = models.DateField(auto_now_add=True)
    concepto = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO, default='efectivo')
    
    def __str__(self):
        return f"{self.fecha} - {self.concepto} - {self.monto} - {self.metodo_pago}"

