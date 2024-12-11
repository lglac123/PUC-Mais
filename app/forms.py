from django import forms

class BuscaAno(forms.Form):
    nome = forms.CharField(label="Código", max_length=100, required=True)
