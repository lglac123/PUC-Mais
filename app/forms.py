from django import forms

class BuscaAno(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100, required=True)

class BuscaQuestoesDireto(forms.Form):
    topico=forms.CharField(label='Topico',max_length=100, required=True)
