from django.urls import path
from .views import *

urlpatterns = [
    path('registro',Registro.as_view(),name='registro'),
]