from django.db import models


class Reserva(models.Model):
    """Representa un bloque de tiempo que se puede reservar."""

    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.fecha} {self.hora} - {self.servicio}"

