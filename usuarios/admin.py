from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    
    list_display = ('nombre_usuario', 'email', 'rol', 'is_staff', 'is_active')
    list_filter = ('rol', 'is_staff', 'is_active')
    search_fields = ('nombre_usuario', 'email')
    ordering = ('nombre_usuario',)
    
    fieldsets = (
        ('Información de Usuario', {
            'fields': ('nombre_usuario', 'email', 'password')
        }),
        ('Rol y Permisos', {
            'fields': ('rol', 'is_staff', 'is_active', 'is_admin', 'is_superadmin')
        }),
        ('Fechas', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)  
        }),
    )
    
    readonly_fields = ('last_login', 'date_joined')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre_usuario', 'email', 'rol', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )  
    exclude = ('groups', 'user_permissions')
    
    def has_module_permission(self, request):
        """Controla si el usuario puede ver el módulo de Usuarios en el admin"""
        if not request.user.is_authenticated:
            return False
        if request.user.is_superadmin or request.user.is_admin:
            return True
        if request.user.rol == 'gerente':
            return True
        return False
    
    def has_add_permission(self, request):
        """Controla si el usuario puede agregar nuevos usuarios"""
        if not request.user.is_authenticated:
            return False
        if request.user.is_superadmin or request.user.is_admin:
            return True
        if request.user.rol == 'gerente':
            return True
        return False
    
    def has_change_permission(self, request, obj=None):
        """Controla si el usuario puede editar usuarios"""
        if not request.user.is_authenticated:
            return False
        if request.user.is_superadmin or request.user.is_admin:
            return True
        if request.user.rol == 'gerente':
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Controla si el usuario puede eliminar usuarios"""
        if not request.user.is_authenticated:
            return False
        if request.user.is_superadmin or request.user.is_admin:
            return True
        if request.user.rol == 'gerente':
            return True
        return False
