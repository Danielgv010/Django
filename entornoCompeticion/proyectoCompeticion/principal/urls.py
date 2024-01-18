from django.urls import path
from . import views

urlpatterns = [
    path('equipos/',views.verEquipos,name='equipos'),
    path('competicion/<int:competicion_id>', views.verCompeticion, name="equiposCompeticion")
]