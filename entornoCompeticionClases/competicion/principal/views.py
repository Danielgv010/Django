from datetime import timezone
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Competicion, Equipo, Jugador
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.

class inicio(TemplateView):
    template_name = 'principal/inicio.html'

class listadoCompeticiones(ListView):
    model = Competicion

@method_decorator(login_required,name="dispatch")
class crearCompeticion(CreateView):
    model = Competicion
    fields = ["nombre","lugar","fecha"]
    success_url = reverse_lazy('listado')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(crearCompeticion, self).form_valid(form)

class listadoEquipo(ListView):
    model = Equipo

class listadoEquipoFilter(ListView):
    model = Equipo


@method_decorator(login_required,name="dispatch")
class crearEquipo(CreateView):
    model = Equipo
    fields = ["nombre","categoria","competicion","responsable"]
    success_url = reverse_lazy('listado')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(crearEquipo, self).form_valid(form)

@method_decorator(login_required,name="dispatch")
class borrarEquipo(DeleteView):
    model = Equipo
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        equipo = self.get_object() # me devuelve el Competicion que se quiere modificar
        if equipo.responsable != request.user: # comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required,name="dispatch")
class modificarEquipo(UpdateView):
    model = Equipo
    fields = ["nombre","categoria","competicion","responsable"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        Equipo = self.get_object() # me devuelve el Competicion que se quiere modificar
        if Equipo.responsable != request.user: # comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)
    
class listadoJugador(ListView):
    model = Jugador

@method_decorator(login_required,name="dispatch")
class crearJugador(CreateView):
    model = Jugador
    fields = ["nombre","correo","edad","foto","equipo"]
    success_url = reverse_lazy('listado')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(crearJugador, self).form_valid(form)

@method_decorator(login_required,name="dispatch")
class borrarJugador(DeleteView):
    model = Jugador
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        jugador = self.get_object() # me devuelve el Competicion que se quiere modificar
        if jugador.equipo.responsable != request.user: # comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required,name="dispatch")
class modificarJugador(UpdateView):
    model = Jugador
    fields = ["nombre","correo","edad","foto","equipo"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        jugador = self.get_object() # me devuelve el Competicion que se quiere modificar
        if jugador.equipo.responsable != request.user: # comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)

class EquipoDetailView(DetailView):
    model = Equipo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CompeticionDetailView(DetailView):
    model = Competicion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class JugadorDetailView(DetailView):
    model = Jugador

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context