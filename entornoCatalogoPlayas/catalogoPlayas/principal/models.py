from django.db import models

# Create your models here.

class Playa(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    descripcion = models.TextField()
    longitud = models.FloatField()

    def __str__(self):
        return self.nombre + "(" + self.provincia + ")"