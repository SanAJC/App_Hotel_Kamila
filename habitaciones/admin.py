from django.contrib import admin
from .models import Habitacion, Venta_Habitacion,Huesped
# Register your models here.


@admin.register(Huesped)
class HuespedAdmin(admin.ModelAdmin):
    list_display = ('primer_nombre', 'primer_apellido', 'telefono', 'cedula')
    list_filter = ('primer_nombre', 'primer_apellido', 'telefono')
    search_fields = ('primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'cedula', 'telefono')
    ordering = ('primer_nombre',)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero',  'precio', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('numero',)  # Solo campos de texto se pueden buscar
    ordering = ('numero',)

@admin.register(Venta_Habitacion)
class Venta_HabitacionAdmin(admin.ModelAdmin):
    list_display = ('habitacion', 'huesped', 'tipo_estadia', 'precio_pagado', 'fecha_entrada', 'fecha_salida')
    list_filter = ('habitacion', 'huesped', 'tipo_estadia', 'precio_pagado', 'fecha_entrada', 'fecha_salida')
    search_fields = ('habitacion__numero', 'huesped__primer_nombre', 'huesped__primer_apellido', 'huesped__cedula')
    ordering = ('-fecha_entrada',)
    list_per_page = 10
    
    # Autocomplete para seleccionar huesped y habitación
    autocomplete_fields = ['huesped', 'habitacion']
    

