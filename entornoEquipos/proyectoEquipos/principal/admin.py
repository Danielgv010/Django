from django.contrib import admin
from .models import Competicion, Equipo, Jugador
# Register your models here.

class CompeticionAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","lugar","fecha","creado","modificado")

admin.site.register(Competicion,CompeticionAdmin)

class EquipoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","categoria","responsable","creado","modificado")

admin.site.register(Equipo,EquipoAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","correo","edad","foto","equipo","creado","modificado")

admin.site.register(Jugador,JugadorAdmin)