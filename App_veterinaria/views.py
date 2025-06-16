from django.shortcuts import render, get_object_or_404, redirect

from .models import Reserva

# Create your views here.se crea primero la vista luego se agrega la urls en e l modulo
def base(request):
    return render(request, 'app/base.html')
def servicio(request):
    return render(request, 'app/servicios.html')
def reserva_hora(request):
    horas = Reserva.objects.filter(disponible=True).order_by("fecha", "hora")
    return render(request, 'app/reserva_hora.html', {"horas": horas})


def reservar(request, id):
    """Marca la hora como tomada."""
    hora = get_object_or_404(Reserva, id=id, disponible=True)
    hora.disponible = False
    hora.save()
    return redirect('reserva_hora')
def contacto(request):
    return render(request, 'app/contacto.html')
def quienes_somos(request):
    return render(request, 'app/quienes_somos.html')

