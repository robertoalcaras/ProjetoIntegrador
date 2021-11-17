from django.urls import path
from . import views
from clinicafono.urls import *

urlpatterns = [
    #path('', views.index, name='index'),
    path("paciente/", views.paciente, name='paciente'),
    

    
]
