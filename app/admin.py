from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario,Huesped,Habitacion,Producto,Venta_Habitacion,Venta_Producto,Orden_Lavanderia

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    
    list_display = ('nombre_usuario', 'email', 'rol')
    list_filter = ('rol','nombre_usuario')
    search_fields = ('nombre_usuario',  'email')
    ordering = ('nombre_usuario',)

@admin.register(Huesped)
class HuespedAdmin(admin.ModelAdmin):
    list_display = ('primer_nombre', 'primer_apellido', 'cedula', 'telefono')
    list_filter = ('primer_nombre', 'primer_apellido')
    search_fields = ('primer_nombre', 'primer_apellido', 'cedula')
    ordering = ('primer_nombre',)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'precio', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('numero',)
    ordering = ('numero',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    list_filter = ('cantidad',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Venta_Habitacion)
class Venta_HabitacionAdmin(admin.ModelAdmin):
    list_display = ('huesped', 'habitacion', 'fecha_entrada', 'fecha_salida', 'precio_pagado', 'metodo_pago', 'extras')
    list_filter = ('fecha_entrada', 'fecha_salida')
    search_fields = ('huesped__primer_nombre', 'habitacion__numero')
    ordering = ('fecha_entrada',)

@admin.register(Venta_Producto)
class Venta_ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'precio_pagado', 'metodo_pago')
    list_filter = ('producto', 'metodo_pago')
    search_fields = ('producto__nombre',)
    ordering = ('producto',)

@admin.register(Orden_Lavanderia)
class Orden_LavanderiaAdmin(admin.ModelAdmin):
    list_display = ('huesped', 'cantidad_prendas', 'valor_por_prenda', 'valor_total', 'estado')
    list_filter = ('estado',)
    search_fields = ('huesped__primer_nombre',)
    ordering = ('huesped',)
