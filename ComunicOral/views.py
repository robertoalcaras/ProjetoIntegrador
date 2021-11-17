from django.shortcuts import render, redirect
from ComunicOral.forms import ComunicOralForm
from ComunicOral.models import ComunicOral

def comunicoral(request):
    if request.method == 'GET':
        comunicorals = ComunicOral.objects.all()
        form = ComunicOralForm()
        context = {
            'comunicorals': comunicorals,
            'form': form,
        }
        
        return render(request, 'comunicoral.html', context=context)
    elif request.method == 'POST':
        form = ComunicOralForm(request.POST)
        
        if form.is_valid():
            comunic = form.save()
            form = ComunicOralForm()
        
        context = {
            'form': form
        }
        
        return render(request, 'comunicoral.html', context=context)



