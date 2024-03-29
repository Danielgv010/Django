from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20,verbose_name="Nombre de la categoria")
    descripcion = models.CharField(max_length=100, verbose_name="Descripcion de la categoria")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del artículo")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación del artículo")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["-creado"]

class Articulo(models.Model):
    titulo = models.CharField(max_length=100,verbose_name="Título del artículo")
    texto = models.TextField(verbose_name="Contenido del artículo")
    imagen = models.ImageField(verbose_name="Foto del artículo",null=True,blank=True,upload_to="fotos")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del artículo")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación del artículo")
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria,verbose_name="Categorias")

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ["-creado"]

class Comentario(models.Model):
    texto = models.TextField(verbose_name="Comentario del artículo")
    articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del comentario")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación del comentario")

    def __str__(self):
        return self.texto[:10]+"..."

    class Meta:
        ordering = ["-creado"]