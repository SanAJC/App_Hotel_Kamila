from django.contrib import admin
from .models import Orden_Lavanderia

@admin.register(Orden_Lavanderia)
class LavanderiaAdmin(admin.ModelAdmin):
    list_display = ('huesped', 'cantidad_prendas', 'valor_total', 'estado')
    list_filter = ('huesped', 'cantidad_prendas', 'valor_total', 'estado')
    search_fields = ('huesped', 'cantidad_prendas', 'valor_total', 'estado')
    ordering = ('huesped',)
