from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Moto

# Create your views here.

def mostarMotos(request):
    motos = loader.get_template("principal\listado.html")

    contexto = {
        'motos':Moto.objects.all(),
    }
    return HttpResponse(motos.render(contexto,request))