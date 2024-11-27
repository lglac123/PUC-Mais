from django import forms
from django import forms

class BuscaAno(forms.Form):
    ano = forms.CharField(label="Ano", max_length=4, required=True)