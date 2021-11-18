"""clinicafono URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Pattern
from django import urls
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paciente.urls')),
    path('', include('ProfissionalEnc.urls')),
    path('', include('ComunicOral.urls')),
    path('', include('avaliacaoAD.urls')),
    path('', include('tipodevoz.urls')),
    path('', include('ressonancia.urls')),
    path('', include('ataquevocal.urls')),
    path('', include('pitch.urls')),
    path('', include('loudness.urls')),
    #path('', include('paciente.urls')),
]
