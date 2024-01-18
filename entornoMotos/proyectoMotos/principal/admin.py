from django.contrib import admin
from .models import Moto

# Register your models here.

class MotoAdmin(admin.ModelAdmin):
    list_display = ("precio","marca","modelo","localidad","fecha_fabricacion","kilometros",)
    list_filter = ("marca","localidad",)
    search_fields = ("marca","modelo","localidad",)

admin.site.register(Moto, MotoAdmin)