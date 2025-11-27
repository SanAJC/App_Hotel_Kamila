from django.db import models

class Huesped(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15 , unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"