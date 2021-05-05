from django import forms
from django.forms import ModelForm
from .models import *
from team.models import *

class CitasForms(ModelForm):
    class Meta:
        model = Citas
        fields = '__all__'
        #exclude = ('asesor',)
        widgets = {'asesor': forms.HiddenInput()}
        labels = {
            "whattsapp": "Recibir mensaje de Whattsapp?  "
        }

class CasaForms(ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Casa
        fields = '__all__'
        exclude = ('created',)
        #widgets = {'vendedor': forms.HiddenInput()}
        labels = {
            "precio": "Precio de inmueble (En MXN) ",
            "amenidades": "El inmueble cuenta con amenidades? ",
            "termino": "Ya se vendio el Inmueble?",
            "notas": "Aqui puedes poner una breve descripcion del Inmueble"
        }

class FotosCasaForms(ModelForm):
    class Meta:
        model = CasaImagen
        fields = '__all__'


class DepaForms(ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Departamentos
        fields = '__all__'
        exclude = ('created',)
        #widgets = {'vendedor': forms.HiddenInput()}
        labels = {
            "precio": "Precio de inmueble (En MXN) ",
            "amenidades": "El inmueble cuenta con amenidades? ",
            "termino": "Ya se vendio el Inmueble?",
            "notas": "Aqui puedes poner una breve descripcion del Inmueble"
        }


class ComercioForms(ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Comercio
        fields = '__all__'
        exclude = ('created',)
        #widgets = {'vendedor': forms.HiddenInput()}
        labels = {
            "precio": "Precio de inmueble (En MXN) ",
            "amenidades": "El inmueble cuenta con amenidades? ",
            "termino": "Ya se vendio el Inmueble?",
            "notas": "Aqui puedes poner una breve descripcion del Inmueble"
        }


class TerrenoForms(ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Terreno
        fields = '__all__'
        exclude = ('created',)
        #widgets = {'vendedor': forms.HiddenInput()}
        labels = {
            "precio": "Precio de inmueble (En MXN) ",
            "amenidades": "El inmueble cuenta con amenidades? ",
            "termino": "Ya se vendio el Inmueble?",
            "notas": "Aqui puedes poner una breve descripcion del Inmueble"
        }