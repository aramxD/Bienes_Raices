from django.shortcuts import render, get_object_or_404
from .models import *

def listado_paginas(request):
    paginas = Pagina.objects.all()
    context= {
        'paginas' : paginas,
    }
    return render(request, 'listado_paginas.html', context)

def pagina(request, slug):
    pagina = get_object_or_404(Pagina, slug=slug)

    context = {
        'pagina' : pagina,
    }
    return render(request, 'pagina.html', context)
# Create your views here.
