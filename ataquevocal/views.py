from django.shortcuts import render
from ataquevocal.forms import AtaqueVocalForm
from ataquevocal.models import AtaqueVocal
# Create your views here.

def ataquevocal(request):
    if request.method =='GET':
        
        ataquevocals = AtaqueVocal.objects.all()
        
        form = AtaqueVocalForm()
        
        context = {
            'ataquevocals' : ataquevocals,
            'form' : form,
        }
        return render (request, 'ataquevocal.html', context=context)
    elif request.method == 'POST':
        
        form = AtaqueVocalForm(request.POST)
        
        if form.is_valid():
            
            ataquev = form.save()
            form = AtaqueVocalForm()
        
        context = {
            'form' : form
        }    
        return render(request, 'ataquevocal.html', context=context)
        