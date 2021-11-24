from django.urls import path
from . import views
from clinicafono.urls import *

urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("ProfissionalEnc/", views.profissionalenc, name='profissionalenc'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),
    path('verprofissional/<int:pk>/', views.verprofissional, name='verprofissional'),
    path('editprofissional/<int:pk>/', views.editprofissional, name='editprofissional'),
    path('updateprofissional/<int:pk>/', views.updateprofissional, name='updateprofissional'),
    path('deleteprofissional/<int:pk>/', views.deleteprofissional, name='deleteprofissional'),

    
]
