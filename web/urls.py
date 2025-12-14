from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('habitaciones/', views.habitaciones_listado, name='habitaciones'),
]