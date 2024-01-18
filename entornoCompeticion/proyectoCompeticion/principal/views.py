from django.http import HttpResponse
from django.shortcuts import render
from .models import Equipo, Competicion
from django.template import loader
from django.shortcuts import get_object_or_404

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