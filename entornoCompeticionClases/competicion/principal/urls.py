from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio.as_view(),name='inicio'),
    path('listado/',listadoCompeticiones.as_view(),name='listado'),
    path('listadoEquipo/',listadoEquipo.as_view(),name='listadoEquipo'),
    path('listadoJugador/',listadoJugador.as_view(),name='listadoJugador'),
    path('crearCompeticion/',crearCompeticion.as_view(),name='crear'),
    path('crearEquipo/',crearEquipo.as_view(),name='crearEquipo'),
    path('crearJugador/',crearJugador.as_view(),name='crearJugador'),
    path('borrarEquipo/<int:pk>',borrarEquipo.as_view(),name='borrarEquipo'),
    path('modificarEquipo/<int:pk>',modificarEquipo.as_view(),name='modificarEquipo'),
]