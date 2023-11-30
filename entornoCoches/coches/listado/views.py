from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def listadoCoches(request):
    coches = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020, "color": "Rojo"},
        {"marca": "Ford", "modelo": "Mustang", "año": 2021, "color": "Azul"},
        {"marca": "Volkswagen", "modelo": "Golf", "año": 2019, "color": "Blanco"},
        {"marca": "Honda", "modelo": "Civic", "año": 2018, "color": "Negro"},
        {"marca": "Tesla", "modelo": "Model 3", "año": 2022, "color": "Plata"}
    ]
    plantilla = loader.get_template("listadoEnTabla.html")
    contexto = {
        "listaCoches":coches,
    }
    return HttpResponse(plantilla.render(contexto, request))
