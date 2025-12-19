from django.contrib import admin
from .models import Gasto

# Register your models here.

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'concepto', 'monto', 'metodo_pago')
    list_filter = ('fecha', 'metodo_pago')
    search_fields = ('concepto',)
