from django.urls import  path
from .views import *

urlpatterns = [    
    
    path('registro/', registro, name='registro'),
    path('login/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logoutuser'),
]