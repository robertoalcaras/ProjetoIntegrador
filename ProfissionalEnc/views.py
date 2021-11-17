from django.shortcuts import redirect, render
from django.http import HttpResponse
from ProfissionalEnc.forms import ProfissionalEncForm
from ProfissionalEnc.models import ProfissionalEnc
#from paciente.models import Paciente

def profissionalenc(request):
    if request.method == 'GET':
        profissionalencs = ProfissionalEnc.objects.all()
        
        form = ProfissionalEncForm()
        
        context = {
            'profissionalencs' : profissionalencs,
            'form' : form,
        }

        return render(request, 'profissionalenc.html', context=context)
    elif request.method == 'POST':
        form = ProfissionalEncForm(request.POST)
        
        if form.is_valid():
                        
            profissional = form.save()
            form = ProfissionalEncForm()
                     
        context = {
           
           'form' : form,
        }
        return render(request, 'profissionalenc.html', context=context)

def update(request, profissionalenc_id):
    if request.method == 'GET':
        profissionalencs = ProfissionalEnc.objects.all()
        profissionalenc = ProfissionalEnc.objects.filter(id=profissionalenc_id).first()
        
        form = ProfissionalEncForm(instance=profissionalenc)
        context = {
            'profissionalencs' : profissionalencs,
            'form' : form,
        }

        return render(request, 'profissionalenc.html', context)
          
    elif request.method == 'POST':
        profissionalenc = ProfissionalEnc.objects.filter(id=profissionalenc_id).first()
        form = ProfissionalEncForm(request.POST, instance=profissionalenc)
        if form.is_valid():
            form.save()
            #return redirect('/')
        else:
            profissionalencs = ProfissionalEnc.objects.all()
     
            context = {
                'profissionalencs' : profissionalencs,
                'form' : form,
            }
            return render(request, 'profissionalenc.html', context)
        