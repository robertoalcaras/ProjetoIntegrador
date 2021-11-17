from django.shortcuts import render
from tipodevoz.forms import TipoVozForm
from tipodevoz.models import TipoVoz

def tipodevoz(request):
    if  request.method == 'GET':
        
        tipovozs = TipoVoz.objects.all()
        
        form = TipoVozForm()
        
        context = {
            'tipovozs' : tipovozs,
            'form' : form,
        }
        return render(request, 'tipodevoz.html', context=context)
    elif request.method == 'POST':
        form = TipoVozForm(request.POST)
        
        if form.is_valid():
            
            tipov = form.save()
            form = TipoVozForm()
        
        context = {
            'form': form
        }
        return render(request, 'tipodevoz.html', context=context)
    