from django import forms
from django.forms import ModelForm
from team.models import *


class PerfilForm(ModelForm):
    class Meta:
        model = Asesor
        fields = '__all__'
        exclude = ('user', 'nombre', 'apeido', 'apodo', 'email')
        #widgets = {'foto': forms.HiddenInput(),}
        labels = {
            "foto": "Imagen para Perfil, debe ser cuadrada  "
        }

