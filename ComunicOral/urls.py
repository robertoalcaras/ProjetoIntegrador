from django.urls import path
from . import views
from clinicafono.urls import *

urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("comunicoral/", views.comunicoral, name='comunicoral'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),
    

    
]