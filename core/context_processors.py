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
        
        hoy_inicio = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        hoy_fin = hoy_inicio + timedelta(days=1)
        
        from django.db.models.functions import Coalesce
        
        ventas_hoy = Venta_Habitacion.objects.filter(
            fecha_entrada__gte=hoy_inicio,  # Desde las 00:00 de hoy
            fecha_entrada__lt=hoy_fin        # Hasta las 23:59 de hoy
        ).aggregate(
            total_precio=Coalesce(Sum('precio_pagado'), Decimal('0')),
            total_extras=Coalesce(Sum('extras'), Decimal('0'))
        )
        
        # Total = precio_pagado + extras
        total_ventas = (ventas_hoy.get('total_precio', Decimal('0')) + 
                       ventas_hoy.get('total_extras', Decimal('0')))
        
        context['ventas_del_dia'] = total_ventas
        
    except Exception as e:
        # Si hay algún error, devolver valores por defecto
        context['habitaciones_disponibles'] = 0
        context['habitaciones_ocupadas'] = 0
        context['total_habitaciones'] = 0
        context['ventas_del_dia'] = Decimal('0')
    
    return context
