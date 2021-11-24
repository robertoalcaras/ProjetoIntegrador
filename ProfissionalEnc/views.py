from django.shortcuts import redirect, render
from django.http import HttpResponse
from ProfissionalEnc.forms import ProfissionalEncForm
from ProfissionalEnc.models import ProfissionalEnc
from django.core.paginator import Paginator
#from paciente.models import Paciente

def profissionalenc(request):
    if request.method == 'GET':
        profissionalencs = ProfissionalEnc.objects.all()
        form = ProfissionalEncForm()
        context = {
            'profissionalencs' : profissionalencs,
            'form' : form,
        }
        return render(request, 'profissionalenc.html', context)
    elif request.method == 'POST':
        form = ProfissionalEncForm(request.POST)
        if form.is_valid():
            profissional = form.save()
            form = ProfissionalEncForm()
        context = { 
           'form' : form,
        }
        return render(request, 'profissionalenc.html', context=context)

def verprofissional(request, pk):
    data = {}
    data['prof'] = ProfissionalEnc.objects.get(pk=pk)
    return render(request, 'verprofissional.html', data) 

def editprofissional(request, pk):
    data = {}
    data['prof'] = ProfissionalEnc.objects.get(pk=pk)
    data['form'] = ProfissionalEncForm(instance=data['prof'])
    return render(request, 'profissionalenc.html', data) 
    #return render(request, 'profissionalenc.html', data)
    return redirect('ProfissionalEnc')

def updateprofissional(request, pk):
    data = {}
    data['prof'] = ProfissionalEnc.objects.get(pk=pk)
    form = ProfissionalEncForm(request.POST, instance=data['prof'])
    if form.is_valid():
        form.save()
        return redirect('profissionalenc')  

def deleteprofissional(request, pk):
    prof = ProfissionalEnc.objects.get(pk = pk)
    prof.delete() 
    return redirect('profissionalenc') 

def paginacao(request):
    data = {}
    all = ProfissionalEnc.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'profissionalenc.html', data)

def busca(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = ProfissionalEnc.objects.filter(nome__icontains=search)
    else:
        data['db'] = ProfissionalEnc.objects.all()
     
    return render(request, 'profissionalenc.html', data)

"""def update(request, profissionalenc_id):
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
"""        