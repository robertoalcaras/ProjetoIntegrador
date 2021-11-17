from django.shortcuts import redirect, render
from django.http import HttpResponse
from paciente.forms import PacienteForm
 
from paciente.models import Paciente

def index(request):
    return HttpResponse('<h1>Clinica de Fonoaudiologia</h1')

def paciente(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        
        form = PacienteForm()
        context = {
            'pacientes': pacientes,
            'form': form,
        }
        return render(request, 'paciente.html', context)
    elif request.method == 'POST':
         form = PacienteForm(request.POST)
         if  form.is_valid():
             cad_paciente = form.save()
             form = PacienteForm()
         
                
        #form = PacienteForm()
         context = {
            'form': form,
             }
         return render(request, 'paciente.html', context=context)