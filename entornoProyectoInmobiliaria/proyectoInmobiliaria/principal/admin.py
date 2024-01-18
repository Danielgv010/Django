from django.contrib import admin
from .models import Piso, Cliente

class PisoAdmin(admin.ModelAdmin):
    list_display = ("numReferencia","poblacion","direccion","precio","fechaAlta","fechaModificacion",)
    list_filter = ("poblacion","cp",)
    search_fields = ("poblacion",)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellidos","correo","telefono",)
    search_fields = ("nombre","apellidos",)
# Register your models here.

admin.site.register(Piso, PisoAdmin)
admin.site.register(Cliente, ClienteAdmin)