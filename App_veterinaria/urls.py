from django import views
from django.urls import path
from .views import base, servicio, reserva_hora, contacto, quienes_somos

urlpatterns = [
    path('', base, name='inicio'),
    path('servicio/', servicio, name='servicio'),
    path('reserva_hora/', reserva_hora, name='reserva_hora'),
    path('contacto/', contacto, name='contacto'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
   
]