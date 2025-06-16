from django.contrib import admin

from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "hora", "servicio", "disponible")
