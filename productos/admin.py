from django.contrib import admin
from .models import Producto, Venta_Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    list_filter = ('nombre', 'precio', 'cantidad')
    search_fields = ('nombre', 'precio', 'cantidad')
    ordering = ('nombre',)

@admin.register(Venta_Producto)
class Venta_ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'huesped', 'cantidad', 'precio_pagado', 'metodo_pago', 'fecha_venta')
    list_filter = ('producto', 'huesped', 'cantidad', 'precio_pagado', 'metodo_pago', 'fecha_venta')
    search_fields = ('producto', 'huesped', 'cantidad', 'precio_pagado', 'metodo_pago', 'fecha_venta')
    ordering = ('producto',)
