from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    
    list_display = ('nombre_usuario', 'email', 'rol')
    list_filter = ('rol','nombre_usuario')
    search_fields = ('nombre_usuario',  'email')
    ordering = ('nombre_usuario',)
