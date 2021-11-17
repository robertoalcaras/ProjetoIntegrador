from django import forms
from ProfissionalEnc.models import ProfissionalEnc

class ProfissionalEncForm(forms.ModelForm):
    class Meta:
       model = ProfissionalEnc
       fields = '__all__'