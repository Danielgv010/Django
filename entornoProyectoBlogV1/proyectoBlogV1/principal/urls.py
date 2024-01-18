from django.urls import path
from . import views

urlpatterns = [
    path('articulos/',views.listadoArticulos,name='listado'),
    path('categoria/<int:categ_id>', views.articulosXcategoria, name="artxcatg")
]