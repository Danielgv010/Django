from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def verPlantilla(request):
    plantilla = loader.get_template("base/plantilla.html")
    contexto = {
        "escribe": True,
        "presenta": "letras",
        "listaNumeros": [10, 20, 30, 40],
        "listaLetras": ["a", "b", "c"]
    }
    return HttpResponse(plantilla.render(contexto, request))


def estructura(request):
    plantilla = loader.get_template("base/estructura.html")
    contexto = {
        "listaLetras": ["a", "b", "c"]
    }
    return HttpResponse(plantilla.render(contexto, request))
