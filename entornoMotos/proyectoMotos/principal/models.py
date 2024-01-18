from django.db import models

# Create your models here.

class Moto(models.Model):
    nombre_vendedor = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.CharField(max_length=9)
    precio = models.FloatField()
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    foto = models.FileField()
    localidad = models.CharField(max_length=30)
    fecha_fabricacion = models.DateField()
    kilometros = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_vendedor
