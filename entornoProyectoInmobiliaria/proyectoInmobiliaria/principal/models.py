from django.db import models

# Create your models here.

class Piso(models.Model):
    #Crear los campos del modelo, un campo corresonde con una columna de la tabla "principal_piso"
    numReferencia = models.CharField(max_length=20,unique=True)
    imagenPiso = models.ImageField(verbose_name="Imagen del piso", null=True, blank=True, upload_to="imgPisos")
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=80)
    cp = models.CharField(max_length=10)
    precio = models.FloatField()
    metroscuadrados = models.IntegerField()
    numHabitaciones = models.IntegerField()
    planta = models.IntegerField()
    banios = models.IntegerField()
    ascensor = models.BooleanField()
    garage = models.BooleanField()
    terraza = models.BooleanField()
    descCorta = models.CharField(max_length=200)
    comentario = models.TextField()
    correoContacto = models.EmailField()
    fechaAlta = models.DateField(auto_now_add=True,verbose_name="Fecha de alta")
    fechaModificacion = models.DateField(auto_now=True,verbose_name="Fecha de modificación")

    def __str__(self):
        return self.numReferencia + " ( " + self.poblacion + " ) "
    
    class Meta:
        ordering = ["poblacion","cp"]

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    correo = models.EmailField()
    telefono = models.CharField(max_length=9)
    inversor = models.BooleanField()

    def __str__(self):
        return self.nombre + " " + self.apellidos
    
    class Meta:
        ordering = ["nombre","apellidos"]