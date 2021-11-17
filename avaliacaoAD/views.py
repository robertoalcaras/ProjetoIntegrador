from django.forms.models import inlineformset_factory
from django.shortcuts import render, get_object_or_404

from ComunicOral.forms import ComunicOralForm
from ressonancia.models import Ressonancia
from tipodevoz.forms import TipoVozForm
from .models import AtaqueVocalCad, AvaliacaoAD, ComunicOralidade, ComunicOral, RessonanciaCad, TipoVozCad, AtaqueVocalCad
from avaliacaoAD.forms import AtaqueVocalCadForm, AvaliacaoAD, AvaliacaoADForm, ComunicOralidadeForm, RessonanciaCadForm, TipodeVozCadForm, AtaqueVocalCadForm


def avaliacaoad(request):
    if request.method == 'GET':
        avaliacaoads = AvaliacaoAD.objects.all()
        comunicoralidades = ComunicOralidade.objects.all()
        form = AvaliacaoADForm()
        formoralidade_factory = inlineformset_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm, extra=9)
        formtipodevozcad_factory = inlineformset_factory(AvaliacaoAD, TipoVozCad, form=TipodeVozCadForm, extra=11)
        formressoanacia_factory = inlineformset_factory(AvaliacaoAD, RessonanciaCad, form=RessonanciaCadForm, extra=4)
        formataquevocal_factory = inlineformset_factory(AvaliacaoAD, AtaqueVocalCad, form=AtaqueVocalCadForm, extra=3)
        #formpitch_factory = inlineformset_factory(AvaliacaoAD, Pi)
        formoralidade = formoralidade_factory()
        formtipodevozcad = formtipodevozcad_factory()
        formressonanciacad = formressoanacia_factory()
        formataquevocalcad = formataquevocal_factory()
        context = {
            'avaliacaoads': avaliacaoads,
            'form': form,
            'formoralidade': formoralidade,
            'formtipodevozcad' : formtipodevozcad,
            'formressonanciacad' : formressonanciacad,
            'formataquevocalcad' : formataquevocalcad,
        }
        return render(request, 'avaliacaoad.html', context=context)
    elif request.method == 'POST':
        form = AvaliacaoADForm(request.POST)
        formoralidade_factory = inlineformset_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm)
        formtipodevozcad_factory = inlineformset_factory(AvaliacaoAD, TipoVozCad, form=TipodeVozCadForm)
        formressoanacia_factory = inlineformset_factory(AvaliacaoAD, RessonanciaCad, form=RessonanciaCad)
        formataquevocal_factory = inlineformset_factory(AvaliacaoAD, RessonanciaCad, form=AtaqueVocalCad)
        formoralidade = formoralidade_factory(request.POST)
        formtipodevozcad = formtipodevozcad_factory(request.POST)
        formressonanciacad = formressoanacia_factory(request.POST)
        formataquevocalcad = formataquevocal_factory(request.POST)
        if form.is_valid() and formoralidade.is_valid() and formtipodevozcad.is_valid() and formressonanciacad.is_valid() and formataquevocalcad.is_valid():
            avaliacao = form.save()
            formoralidade.instance = avaliacao
            formtipodevozcad.instance = avaliacao
            formressonanciacad.instance = avaliacao
            formataquevocalcad.instance = avaliacao
            formoralidade.save()
            formtipodevozcad.save()
            formressonanciacad.save()
            formataquevocalcad.save()
            form = AvaliacaoADForm()
            formoralidade = ComunicOralidadeForm()
            formtipodevozcad = TipodeVozCadForm()
            formressonanciacad = RessonanciaCadForm()
            formataquevocalcad = AtaqueVocalCadForm()
        context = {
            'form' : form,
            'formoralidade' : formoralidade,
            'formtipodevozcad': formtipodevozcad,
            'formressonanciacad': formressonanciacad,
            'formataquevocalcad' : formataquevocalcad,
        }
        
        return render(request, 'avaliacaoad.html', context=context)


