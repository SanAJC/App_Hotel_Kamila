from django.db.models import Count, Q, Sum
from decimal import Decimal


def dashboard_context(request):
    """
    Context processor para proporcionar datos del dashboard al admin
    """
    if not request.path.startswith('/admin'):
        return {}
    
    context = {}
    
    try:
        from habitaciones.models import Habitacion, Venta_Habitacion
        from django.utils import timezone
        from datetime import datetime, timedelta
        
        # Estadísticas de habitaciones
        habitaciones_stats = Habitacion.objects.aggregate(
            total=Count('id'),
            disponibles=Count('id', filter=Q(disponible=True)),
            ocupadas=Count('id', filter=Q(disponible=False)),
        )
        
        context['habitaciones_disponibles'] = habitaciones_stats.get('disponibles', 0)
        context['habitaciones_ocupadas'] = habitaciones_stats.get('ocupadas', 0)
        context['total_habitaciones'] = habitaciones_stats.get('total', 0)
        
        # Ventas del día - suma de ventas de habitaciones del día actual
        hoy = timezone.now().date()
        ventas_hoy = Venta_Habitacion.objects.filter(
            fecha_entrada__date=hoy
        ).aggregate(
            total=Sum('precio_pagado')
        )
        
        context['ventas_del_dia'] = ventas_hoy.get('total') or Decimal('0')
        
    except Exception as e:
        # Si hay algún error, devolver valores por defecto
        context['habitaciones_disponibles'] = 0
        context['habitaciones_ocupadas'] = 0
        context['total_habitaciones'] = 0
        context['ventas_del_dia'] = Decimal('0')
    
    return context
