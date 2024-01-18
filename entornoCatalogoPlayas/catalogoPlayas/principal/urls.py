from django.urls import path
from .views import Catalogo, Detalle, Crear, Modificar, Borrar

urlpatterns = [
    path('', Catalogo.as_view(), name="catalogo"),
    path('playa/<int:pk>', Detalle.as_view(), name="detalle"),
    path('crear-playa', Crear.as_view(), name='crear-playa'),
    path('editar-playa/<int:pk>', Modificar.as_view(), name='editar-playa'),
    path('borrar-playa/<int:pk>', Borrar.as_view(), name='borrar-playa'),
]
