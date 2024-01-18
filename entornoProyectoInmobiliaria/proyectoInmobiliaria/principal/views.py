from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Piso, Cliente

# Create your views here.

def catalogo(request):
    catalogo = loader.get_template("principal\catalogo.html")

    contexto = {
        'pisos':Piso.objects.all(),
        'clientes':Cliente.objects.all(),
    }
    return HttpResponse(catalogo.render(contexto,request))

def crearCliente(request):

    cli = Cliente(nombre="Pepe",apellidos="Fernandez Fernandez", telefono="666999222", correo="pepe@gmail.com", inversor=False)

    cli.save()

    return HttpResponseRedirect(reverse('catalogo'))

def modificarCliente(request):
    try:
        cli = Cliente.objects.get(id=1)
        cli.telefono = '111222333'
        cli.save()
    except:
        pass

    return HttpResponseRedirect(reverse('catalogo'))

def borrarCliente(request):
    try:
        cli = Cliente.objects.get(id=10)
        cli.delete()
    except:
        pass

    return HttpResponseRedirect(reverse('catalogo'))

def borrarPepes(request):
    cliPepes = Cliente.objects.filter(nombre__exact = "Pepe")
    for pep in cliPepes:
        pep.delete()
    return HttpResponseRedirect(reverse('catalogo'))

# def borrarPepes(request):
#     catalogo = loader.get_template("principal\catalogo.html")
#     cliPepes = Cliente.objects.filter(nombre__exact = "Pepe")
#     contexto = {
#         'pisos':Piso.objects.all(),
#         'clientes':cliPepes,
#     }
#     return HttpResponse(catalogo.render(contexto,request))
