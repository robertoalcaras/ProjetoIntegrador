from django.shortcuts import render, resolve_url
from ressonancia.forms import RessonanciaForm

from ressonancia.models import Ressonancia

def ressonancia(request):
    if request.method == "GET":
        
        ressonancias = Ressonancia.objects.all()
        
        form = RessonanciaForm()
        
        context = {
            'ressonancias' : ressonancias,
            'form' : form,
        }
        return render(request, 'ressonancia.html', context=context)
    elif request.method == 'POST':
        
        form = RessonanciaForm(request.POST)
        if form.is_valid():
            
            ressonanciaf = form.save()
            form = RessonanciaForm
        
        context = {
            'form' : form
        }    
        
        return render(request, 'ressonancia.html', context=context)