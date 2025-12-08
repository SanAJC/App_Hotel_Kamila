from django.contrib import admin
from .models import Orden_Lavanderia

@admin.register(Orden_Lavanderia)
class LavanderiaAdmin(admin.ModelAdmin):
    list_display = ('huesped', 'cantidad_prendas', 'valor_total', 'estado', 'fecha_orden')
    list_filter = ('estado', 'fecha_orden')
    search_fields = ('huesped__primer_nombre', 'huesped__primer_apellido', 'huesped__cedula')
    ordering = ('-fecha_orden',)
    
    # Autocomplete para seleccionar huesped
    autocomplete_fields = ['huesped']
