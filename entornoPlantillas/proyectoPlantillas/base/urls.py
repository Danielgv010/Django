from django.urls import path
from . import views

urlpatterns = {
    path("",views.verPlantilla,name="inicial"),
    path("estructura/",views.estructura,name="estructura"),
}