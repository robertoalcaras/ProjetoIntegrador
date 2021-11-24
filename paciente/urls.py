from django.urls import path
from . import views
from clinicafono.urls import *

urlpatterns = [
    path('', views.index, name='index'),
    path("paciente/", views.paciente, name='paciente'),
    path('verpaciente/<int:pk>/', views.verpaciente, name='verpaciente'),
    path('editpaciente/<int:pk>/', views.editpaciente, name='editpaciente'),
    path('updatepaciente/<int:pk>/', views.updatepaciente, name='updatepaciente'),
    path('deletepaciente/<int:pk>/', views.deletepaciente, name='deletepaciente'),
    #path("verpaciente/", views.verpaciente, name='verpaciente'),
    

    
]
