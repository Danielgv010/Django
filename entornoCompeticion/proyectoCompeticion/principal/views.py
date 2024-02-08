from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Equipo, Competicion
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

def verEquipos(request):
    equipos = Equipo.objects.all()

    contexto = {
        "equipos": equipos,
    }

    listado = loader.get_template("principal\equipos.html")

    return HttpResponse(listado.render(contexto,request))


def verCompeticion(request, competicion_id):
    competicion = get_object_or_404(Competicion,id=competicion_id)

    contexto = {
        "equipos": competicion.equipo_set.all(),
    }

    listado = loader.get_template("principal\equipos.html")

    return HttpResponse(listado.render(contexto,request))

class crearEquipo(CreateView):
    model = Equipo
    fields = ["nombre","categoria","competicion","responsable"]
    success_url = reverse_lazy('equipos')

class borrarEquipo(DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipos')

class modificarArticulo(UpdateView):
    pass