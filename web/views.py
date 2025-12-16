from django.shortcuts import render
from habitaciones.models import Habitacion

def index(request):
    # Obtener las habitaciones destacadas
    habitaciones = Habitacion.objects.filter(destacada=True)[:3]
    return render(request, 'pages/index.html', {
        'title': 'Inicio',
        'habitaciones': habitaciones,
    })

def habitaciones_listado(request):
    # Obtener todas las habitaciones
    habitaciones = Habitacion.objects.all()
    
    # Filtros
    capacidad = request.GET.get('capacidad')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    disponible = request.GET.get('disponible')
    
    # Aplicar filtros si existen
    if capacidad:
        if capacidad == '1':
            habitaciones = habitaciones.filter(cantidad_personas=1)
        elif capacidad == '2':
            habitaciones = habitaciones.filter(cantidad_personas=2)
        elif capacidad == '3':
            habitaciones = habitaciones.filter(cantidad_personas__gte=3)
        elif capacidad == '4':
            habitaciones = habitaciones.filter(cantidad_personas__gte=4)
    
    if precio_min:
        habitaciones = habitaciones.filter(precio__gte=precio_min)
    
    if precio_max:
        habitaciones = habitaciones.filter(precio__lte=precio_max)
    
    if disponible == 'true':
        habitaciones = habitaciones.filter(disponible=True)
    elif disponible == 'false':
        habitaciones = habitaciones.filter(disponible=False)
    
    return render(request, 'pages/habitaciones.html', {
        'title': 'Habitaciones',
        'habitaciones': habitaciones,
        'total_habitaciones': habitaciones.count()
    })
