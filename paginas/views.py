from django.shortcuts import render, get_object_or_404
from .models import *

def listado_paginas(request):
    paginas = Pagina.objects.all()
    context= {
        'paginas' : paginas,
    }
    return render(request, 'listado_paginas.html', context)

def pagina(request, slug):
    paginas = Pagina.objects.all()
    pagina = get_object_or_404(Pagina, slug=slug)

    context = {
        'paginas' : paginas,
        'pagina' : pagina,
    }
    return render(request, 'pagina.html', context)


def nueva_pagina(request):
    paginas = Pagina.objects.all()
    

    context = {
        'paginas' : paginas,
        
    }
    return render(request, 'nueva_pagina.html', context)
