from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Articulo
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.

class inicio(TemplateView):
    template_name = 'principal/inicio.html'

class listadoArticulos(ListView):
    model = Articulo

@method_decorator(login_required,name="dispatch")
class crearArticulo(CreateView):
    model = Articulo
    fields = ["titulo","texto","imagen","categorias"]
    success_url = reverse_lazy('listado')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(crearArticulo, self).form_valid(form)

@method_decorator(login_required,name="dispatch")
class borrarArticulo(DeleteView):
    model = Articulo
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        articulo = self.get_object() # me devuelve el articulo que se quiere modificar
        if articulo.autor != request.user: # comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required,name="dispatch")
class modificarArticulo(UpdateView):
    model = Articulo
    fields = ["titulo","texto","imagen","categorias"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        articulo = self.get_object() # me devuelve el articulo que se quiere modificar
        if articulo.autor != request.user: # comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)