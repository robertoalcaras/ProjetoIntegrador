from django.core import paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from paciente.forms import PacienteForm
from paciente.models import Paciente
from django.core.paginator import Paginator

def index(request):
    #return HttpResponse('<h1>Clinica de Fonoaudiologia</h1')
    return render(request, 'index.html')

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
     
def verpaciente(request, pk):
    data = {}
    data['paci'] = Paciente.objects.get(pk=pk)
    return render(request, 'verpaciente.html', data)     

def editpaciente(request, pk):
    data = {}
    data['paci'] = Paciente.objects.get(pk=pk)
    data['form'] = PacienteForm(instance=data['paci'])
    return render(request, 'paciente.html', data)

def updatepaciente(request, pk):
    data = {}
    data['paci'] = Paciente.objects.get(pk=pk)
    form = PacienteForm(request.POST, instance=data['paci'])
    if form.is_valid():
        form.save()
        return redirect('paciente')    
    
def deletepaciente(request, pk):
    paci = Paciente.objects.get(pk = pk)
    paci.delete() 
    return redirect('paciente') 

def paginacao(request):
    data = {}
    all = Paciente.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'paciente.html', data)

def busca(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Paciente.objects.filter(nome__icontains=search)
    else:
        data['db'] = Paciente.objects.all()
     
    return render(request, 'paciente.html', data)