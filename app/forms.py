from django import forms
from django import forms

class BuscaAno(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100, required=True)