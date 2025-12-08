from django.contrib import admin
from .models import Producto, Venta_Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Venta_Producto)
class Venta_ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'huesped', 'cantidad', 'precio_pagado', 'metodo_pago', 'fecha_venta')
    list_filter = ('producto', 'metodo_pago', 'fecha_venta')
    search_fields = ('producto__nombre', 'huesped__primer_nombre', 'huesped__primer_apellido', 'huesped__cedula')
    ordering = ('-fecha_venta',)
    
    # Autocomplete para seleccionar huesped y producto
    autocomplete_fields = ['huesped', 'producto']
