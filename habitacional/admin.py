from django.contrib import admin
from .models import *
# Register your models here.

class CasaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ciudad',  'colonia', 'vendedor', 'precio') #visualizar columnas

class CasaImagenAdmin(admin.ModelAdmin):
    list_display = ('casa', 'id') #visualizar columnas

class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ('id', 'ciudad',  'colonia', 'precio') #visualizar columnas

class DepartamentosImagenAdmin(admin.ModelAdmin):
    list_display = ('casa', 'id') #visualizar columnas

class ComercioAdmin(admin.ModelAdmin):
    list_display = ('id', 'ciudad',  'colonia', 'precio') #visualizar columnas

class ComercioImagenAdmin(admin.ModelAdmin):
    list_display = ('casa', 'id') #visualizar columnas

class TerrenoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ciudad',  'colonia', 'precio') #visualizar columnas

class TerrenoImagenAdmin(admin.ModelAdmin):
    list_display = ('casa', 'id') #visualizar columnas

admin.site.register(Casa, CasaAdmin)
admin.site.register(CasaImagen, CasaImagenAdmin)
admin.site.register(Departamentos, DepartamentosAdmin)
admin.site.register(DepartamentosImagen, DepartamentosImagenAdmin)
admin.site.register(Comercio, ComercioAdmin)
admin.site.register(ComercioImagen, ComercioImagenAdmin)
admin.site.register(Terreno, TerrenoAdmin)
admin.site.register(TerrenoImagen, TerrenoImagenAdmin)