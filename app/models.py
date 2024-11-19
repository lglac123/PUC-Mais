from django.db import models
# from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Course(models.Model):
  name = models.CharField(max_length=40)
  dificulty = models.IntegerField(default=0)
  # Adicionar imagem
  # A relação com a prova já está sendo descrito no ManyToMany do Exam

  def __str__(self):
    return f"{self.name}"


class UserCourse(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  status = models.IntegerField(default=0)

  class Meta:
    unique_together = ('user', 'course')
  
  def __str__(self):
    return f"{self.course.name} - {self.user}"


class Exam(models.Model):
  semester = models.IntegerField(default=1)
  year = models.IntegerField()
  name = models.CharField(max_length=30)
  file = models.FileField()
  courses = models.ManyToManyField(Course)
  video = models.OneToOneField('Video', on_delete=models.CASCADE, blank=True, null=True)


class Topic(models.Model):
  name = models.CharField(max_length=50)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  # list = models.ForeignKey('List', on_delete=models.CASCADE, blank=True) # Não sei se precisa disso de fato. Seria para garantir que um tópico só tem 1 lista no máximo


class Video(models.Model):
  name = models.CharField(max_length=100)
  link = models.URLField()
  description = models.TextField(blank=True)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True)
  # A relação do vídeo com a prova já está descrito no OneToOne no Exam


class List(models.Model):
  name = models.CharField(max_length=50)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Queria [0..1] na List
  # A relação com questão já está descrito no ManyToMany em Question


class Question(models.Model):
  task = models.TextField()
  list = models.ManyToManyField('List')

class Option(models.Model):
  question = models.ManyToManyField(Question)
  text = models.TextField()

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete = models.CASCADE) # Depois
  text = models.TextField()