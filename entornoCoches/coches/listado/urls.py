from django.urls import path
from . import views

urlpatterns = {
    path("coches/",views.listadoCoches,name="coches")
}