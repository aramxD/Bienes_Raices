from django.urls import  path
from .views import *

urlpatterns = [    
    
    path('listado-paginas/', listado_paginas, name='listado_paginas'),
    path('<str:slug>', pagina, name='pagina'),
    path('nueva-pagina/', nueva_pagina, name='nueva_pagina'),

]