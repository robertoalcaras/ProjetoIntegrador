from django.urls import path
from . import views
from clinicafono.urls import *

urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("ressonancia/", views.ressonancia, name='ressonancia'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),

]