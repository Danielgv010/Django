from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Playa
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class Catalogo(ListView):
    model = Playa
    context_object_name = "listaPlayas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        provincia = self.request.GET.get('provincia') or ''
        if provincia:
            context['provincia'] = provincia
        return context

class Detalle(DetailView):
    model = Playa
    context_object_name = "playa"

class Crear(CreateView):
    model = Playa
    fields = '__all__'
    success_url = reverse_lazy('catalogo')

class Modificar(UpdateView):
    model = Playa
    fields = '__all__'
    success_url = reverse_lazy('catalogo')

class Borrar(DeleteView):
    model = Playa
    fields = '__all__'
    success_url = reverse_lazy('catalogo')
    context_object_name = "playa"