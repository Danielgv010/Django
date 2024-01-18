from django.http import HttpResponse
from django.shortcuts import render
from .models import Articulo, Categoria
from django.template import loader
from django.shortcuts import get_object_or_404

# Create your views here.

def listadoArticulos(request):
    #traer de BD todos los articulos
    articulos = Articulo.objects.all()

    #crear un contexto para renderizar la plantilla
    contexto = {
        "articulos":articulos,
    }

    #cargar la plantilla
    listado = loader.get_template('principal/listado.html')

    #devolver el template renderizado con los datos pasados en el contexto
    return HttpResponse(listado.render(contexto,request))

def articulosXcategoria(request, categ_id):
    # Recuperar los articulos de la categoria categ_id
    categoria = get_object_or_404(Categoria,id=categ_id)

    contexto = {
        "nombreCateg":categoria.nombre,
        "articulos":categoria.articulo_set.all()
    }

    #cargar la plantilla
    listado = loader.get_template('principal/listado.html')

    #devolver el template renderizado con los datos pasados en el contexto
    return HttpResponse(listado.render(contexto,request))