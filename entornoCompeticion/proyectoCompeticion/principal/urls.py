from django.urls import path
from . import views
from .views import crearEquipo, borrarEquipo

urlpatterns = [
    path('equipos/',views.verEquipos,name='equipos'),
    path('crear/',crearEquipo.as_view(),name='crear'),
    path('borrar/<int:pk>',borrarEquipo.as_view(),name='borrar'),
    path('modificar/<int:pk>',borrarEquipo.as_view(),name='modificar'),
    path('competicion/<int:competicion_id>', views.verCompeticion, name="equiposCompeticion")
]