from django.urls import path
from . import views

urlpatterns = [
    path("listado/",views.listadoPersonas,name="listado"),
]
