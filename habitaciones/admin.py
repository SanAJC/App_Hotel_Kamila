from django.contrib import admin
from .models import Habitacion, Venta_Habitacion,Huesped
# Register your models here.


@admin.register(Huesped)
class HuespedAdmin(admin.ModelAdmin):
    list_display = ('primer_nombre', 'primer_apellido', 'telefono')
    list_filter = ('primer_nombre', 'primer_apellido', 'telefono')
    search_fields = ('primer_nombre', 'primer_apellido', 'telefono')
    ordering = ('primer_nombre',)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero',  'precio', 'disponible')
    list_filter = ('numero', 'disponible')
    search_fields = ('numero', 'precio', 'disponible')
    ordering = ('numero',)

@admin.register(Venta_Habitacion)
class Venta_HabitacionAdmin(admin.ModelAdmin):
    list_display = ('habitacion', 'huesped', 'tipo_estadia', 'precio_pagado', 'fecha_entrada', 'fecha_salida')
    list_filter = ('habitacion', 'huesped', 'tipo_estadia', 'precio_pagado', 'fecha_entrada', 'fecha_salida')
    search_fields = ('habitacion__numero', 'huesped__primer_nombre', 'huesped__primer_apellido')
    ordering = ('habitacion',)


