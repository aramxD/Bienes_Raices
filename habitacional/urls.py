from django.urls import  path
from .views import *

urlpatterns = [    
    
    path('', home, name='home'),
    path('casa/<int:casa_id>', detalles_casa, name='detalles_casa'),
    path('departamento/<int:depa_id>', detalles_depa, name='detalles_depa'),
    path('comercio/<int:comercio_id>', detalles_comercio, name='detalles_comercio'),
    path('terreno/<int:terreno_id>', detalles_terreno, name='detalles_terreno'),
    

    #Solo STAFF
    path('listado/', listado, name='listado'),
    #Inmuebles (Nuevo + Editar + Eliminar) 
    path('ingreso_casa/', ingreso_casa, name='ingreso_casa'),
    path('editar_casa/<int:casa_pk>', editar_casa, name='editar_casa'),
    path('eliminar_casa/<int:casa_pk>/delete', eliminar_casa, name="eliminar_casa"),
    path('ingreso_casa_foto/', ingreso_casa_foto, name='ingreso_casa_foto'),
    path('eliminar_casa_fotos/<int:foto_pk>/delete', eliminar_casa_fotos, name="eliminar_casa_fotos"),

    path('ingreso_depa/', ingreso_depa, name='ingreso_depa'),
    path('editar_depa/<int:depa_pk>', editar_depa, name='editar_depa'),
    path('eliminar_depa/<int:depa_pk>/delete', eliminar_depa, name="eliminar_depa"),

    path('ingreso_comercio/', ingreso_comercio, name='ingreso_comercio'),
    path('editar_comercio/<int:comercio_pk>', editar_comercio, name='editar_comercio'),
    path('eliminar_comercio/<int:comercio_pk>/delete', eliminar_comercio, name="eliminar_comercio"),

    path('ingreso_terreno/', ingreso_terreno, name='ingreso_terreno'),
    path('editar_terreno/<int:terreno_pk>', editar_terreno, name='editar_terreno'),
    path('eliminar_terreno/<int:terreno_pk>/delete', eliminar_terreno, name="eliminar_terreno"),
]
