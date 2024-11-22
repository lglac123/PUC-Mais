from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Course, Topic


def disciplinas(request):
  courses = Course.objects.all()
  return render(request, 'disciplinas.html', {
    'courses': courses,
  })

def Disciplina(request, course_name):
  course = Course.objects.filter(name=course_name).all() # Pegar o curso a partir do nome no URL
  print(course)
  topic = Topic.objects.filter(course=course[0].id).all() # Pegar todos os tópicos correlacionados a aquele curso
  print(topic)

  return render(request,'Disciplina.html', {
    'topics': topic,
    'course': course[0],
  })

def aulas_listas_basic(request):
  return render(request, "aulas_listas_basic.html")

def home(request):
  return render(request, 'home.html')

@login_required
def provas(request):
  return render(request, "provas_antigas.html")


@login_required
def aulas(request):
  return render(request, "aulas.html")

@login_required
def perfil(request):
  return render(request,'perfil.html')

def createUser(request):
  if request.method == "POST":  
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"],
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  
  return render(request, "register.html", context = {"action": "Adicionar"})


def loginUser(request):
  if request.method == "POST":  
    user = authenticate(
      username = request.POST["username"], 
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context = {"error_msg": "Usuário ou Senha Inválidos"})
    if request.user.is_authenticated:
      return redirect("home")
  return render(request, "login.html")

  
def logoutUser(request):
  logout(request)
  return redirect("home")










