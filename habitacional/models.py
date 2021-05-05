from django.db import models
from team.models import Asesor

# Create your models here.

TIPO_INMUEBLE = (
    ('Departamento', 'Departamento'),
    ('Casa', 'Casa'),)
TIPO_CONTRATO = (
    ('Venta', 'Venta'),
    ('Renta', 'Renta'),)

class Casa(models.Model):
    #Datos del inmueble
    precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    m2_construccion = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    m2_terreno = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    num_habitaciones = models.IntegerField(default=0, verbose_name="Numero de cuartos", blank=True)
    num_banos = models.DecimalField(max_digits=2, decimal_places=1, default=1, verbose_name="Numero de baños", blank=True)
    estacionamiento = models.IntegerField(default=0, verbose_name="Numero de estacionamientos", blank=True)
    amenidades = models.BooleanField(default=False)
    notas = models.TextField(max_length=500, blank=True,)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/landing", blank=True)

    #ubicacion
    calle = models.CharField(max_length=40, blank=True)
    numero_ext = models.CharField(max_length=8, blank=True)
    numero_int = models.CharField(max_length=4, blank=True)
    colonia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40, default='Tijuana')
    estado = models.CharField(max_length=40, default='Baja California')
    pais = models.CharField(max_length=40, default='Mexico')
    codigo_postal = models.CharField(max_length=6, blank=True )
    latitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="Latitud", null=True, blank=True)
    longitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="longitud", null=True, blank=True)
    featured = models.BooleanField(default=True, verbose_name="Quieres que aparesca en la pagina principal?")
    
    #transaccion
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO, default='Venta', max_length=15)
    termino = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    vendedor = models.ForeignKey(Asesor, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        nombre = "Casa "  + self.colonia
        return nombre


class CasaImagen(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/casa")
    alt = models.CharField(max_length=40, blank=True)


class Departamentos(models.Model):
    #Datos del inmueble
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    m2_construccion = models.DecimalField(max_digits=6, decimal_places=2,)
    nivel =  models.IntegerField(verbose_name="Nivel", blank=True)
    num_habitaciones = models.IntegerField(default=0, verbose_name="Numero de cuartos")
    num_banos = models.IntegerField(default=0, verbose_name="Numero de baños")
    estacionamiento = models.IntegerField(default=0, verbose_name="Numero de estacionamientos")
    amenidades = models.BooleanField(default=False)
    notas = models.TextField(max_length=500, blank=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/landing", blank=True)

    #ubicacion
    calle = models.CharField(max_length=40, blank=True)
    numero_ext = models.CharField(max_length=8, blank=True)
    numero_int = models.CharField(max_length=4, blank=True)
    colonia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40, default='Tijuana')
    estado = models.CharField(max_length=40, default='Baja California')
    pais = models.CharField(max_length=40, default='Mexico')
    codigo_postal = models.CharField(max_length=6, blank=True )
    latitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="Latitud", null=True, blank=True)
    longitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="longitud", null=True, blank=True)
    featured = models.BooleanField(default=True, verbose_name="Aparece en el landing>?")
    
    #transaccion
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO, default='Venta', max_length=15)
    termino = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    vendedor = models.ForeignKey(Asesor, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        nombre = "Departamento "  + self.colonia
        return nombre


class DepartamentosImagen(models.Model):
    casa = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/departamentos")
    alt = models.CharField(max_length=40, blank=True)


class Comercio(models.Model):
    #Datos del inmueble
    precio = models.DecimalField(max_digits=12, decimal_places=2,)
    m2_construccion = models.DecimalField(max_digits=6, decimal_places=2,)
    nivel = models.IntegerField(default=0, verbose_name="Nivel")
    num_habitaciones = models.IntegerField(default=0, verbose_name="Numero de cuartos")
    num_banos = models.IntegerField(default=0, verbose_name="Numero de baños")
    estacionamiento = models.IntegerField(default=0, verbose_name="Numero de estacionamientos")
    notas = models.TextField(max_length=500, blank=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/landing", blank=True)

    #ubicacion
    calle = models.CharField(max_length=40, blank=True)
    numero_ext = models.CharField(max_length=8, blank=True)
    numero_int = models.CharField(max_length=4, blank=True)
    colonia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40, default='Tijuana')
    estado = models.CharField(max_length=40, default='Baja California')
    pais = models.CharField(max_length=40, default='Mexico')
    codigo_postal = models.CharField(max_length=6, blank=True )
    latitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="Latitud", null=True, blank=True)
    longitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="longitud", null=True, blank=True)
    featured = models.BooleanField(default=True, verbose_name="Aparece en el landing>?")
    
    #transaccion
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO, default='Venta', max_length=15)
    termino = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    vendedor = models.ForeignKey(Asesor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        nombre = "Comercio "  + self.colonia
        return nombre


class ComercioImagen(models.Model):
    casa = models.ForeignKey(Comercio, on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/comercios")
    alt = models.CharField(max_length=40, blank=True)


class Terreno(models.Model):
    #Datos del inmueble
    precio = models.DecimalField(max_digits=12, decimal_places=2,)
    m2_terreno = models.DecimalField(max_digits=6, decimal_places=2,)
    notas = models.TextField(max_length=500, blank=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/landing", blank=True)

    #ubicacion
    calle = models.CharField(max_length=40, blank=True)
    numero_ext = models.CharField(max_length=8, blank=True)
    numero_int = models.CharField(max_length=4, blank=True)
    colonia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40, default='Tijuana')
    estado = models.CharField(max_length=40, default='Baja California')
    pais = models.CharField(max_length=40, default='Mexico')
    codigo_postal = models.CharField(max_length=6, blank=True )
    latitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="Latitud", null=True, blank=True)
    longitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="longitud", null=True, blank=True)
    featured = models.BooleanField(default=True, verbose_name="Aparece en el landing>?")
    
    #transaccion
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO, default='Venta', max_length=15)
    termino = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    vendedor = models.ForeignKey(Asesor, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        nombre = "Terreno "  + self.colonia
        return nombre


class TerrenoImagen(models.Model):
    casa = models.ForeignKey(Terreno, on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/terrenos")
    alt = models.CharField(max_length=40, blank=True)



    