from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Competicion(models.Model):
    nombre = models.CharField(max_length=30,verbose_name="Nombre de la competicion")
    lugar = models.CharField(max_length=50,verbose_name="Lugar de la competicion")
    fecha = models.DateField(verbose_name="Fecha de la competicion")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del artículo")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación del artículo")

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=30,verbose_name="Nombre del equipo")
    categoria = models.CharField(max_length=30,verbose_name="Categoria del equipo")
    competicion = models.ManyToManyField(Competicion)
    responsable = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Responsable del equipo")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del artículo")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación del artículo")

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=30,verbose_name="Nombre del jugador")
    correo = models.EmailField(verbose_name="Correo del jugador")
    edad = models.IntegerField(verbose_name="Edad del jugador")
    foto = models.ImageField(verbose_name="Foto del jugador")
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del artículo")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación del artículo")

    def __str__(self):
        return self.nombre