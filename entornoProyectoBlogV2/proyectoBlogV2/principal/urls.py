from django.urls import path
from .views import *
urlpatterns = [
    path('',inicio.as_view(),name='inicio'),
    path('listado/',listadoArticulos.as_view(),name='listado'),
    path('crear/',crearArticulo.as_view(),name='crear'),
    path('borrar/<int:pk>',borrarArticulo.as_view(),name='borrar'),
    path('modificar/<int:pk>',modificarArticulo.as_view(),name='modificar'),
    path('categoriaDetalle/<int:pk>',categoriaDetalle.as_view(),name='categoriaDetalle'),
]