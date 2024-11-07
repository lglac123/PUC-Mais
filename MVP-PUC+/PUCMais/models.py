from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class TopMovie(models.Model):
  def __str__(self):
    return f"{self.nome}"
  
  nome = models.CharField(max_length=50)
  icone = models.CharField(max_length=50)
  descricao = models.TextField(max_length=50)
  idade = models.IntegerField()
  sexo = models.CharField(max_length=10) 
  data_nascimento = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Movie(models.Model):
  def __str__(self):
    return f'{self.nome}'

  OPTIONS = [
    ("A", "Ação"),
    ("D", "Drama"),
    ("C", "Comedy"),
    ("R", "Romance"),
    ("H", "Horror")
  ]

  nome = models.CharField(max_length=50)
  link = models.CharField(max_length=150)
  filme = models.ForeignKey(TopMovie, on_delete=models.CASCADE)
  nota = models.FloatField(max_length=2)
  genero = models.CharField(max_length=50,choices=OPTIONS)
  user = models.ForeignKey(User, on_delete=models.CASCADE)