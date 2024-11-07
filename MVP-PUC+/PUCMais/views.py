from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Movie, TopMovie 


def home(request):
  try:
    top_movies = TopMovie.objects.filter(user = request.user).all()
    movies = Movie.objects.filter(user = request.user).all()
    return render(request, "home.html", {"movie": movies, "top_movie": top_movies})
  except:
    top_movies = None
    movies = None
    return redirect("login")

@login_required
def provas(request):
  return render(request, "provas_antigas.html")


@login_required
def aulas(request):
  return render(request, "aulas.html")


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


@login_required
def create_top_movie(request):
  if request.method == "POST":
    TopMovie.objects.create(
    nome = request.POST["nome"],
    icone = request.POST["icone"],
    descricao = request.POST["descricao"],
    idade = request.POST["idade"],
    sexo = request.POST["sexo"],
    data_nascimento = request.POST["data_nascimento"],
    user = request.user
      )
    return redirect(home)
  return render(request, "top_forms.html", context={"type": "Adicionar"})


@login_required
def update_top_movie(request, id):
  tm = TopMovie.objects.get(id = id)
  if request.method == "POST":
    tm.nome = request.POST["nome"]
    tm.icone = request.POST["icone"]
    tm.descricao = request.POST["descricao"]
    tm.idade = request.POST["idade"]
    tm.sexo = request.POST["sexo"]
    tm.data_nascimento = request.POST["data_nascimento"]
    tm.save()
    
    return redirect(home)
  return render(request, "top_forms.html", context={"type": "Atualizar", "top_movie": tm})


@login_required
def delete_top_movie(request, id):
  tm = TopMovie.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      tm.delete()
    return redirect(home)
  return render(request, "confirmacao.html", context={"type": "Remover", "top_movie": tm})


@login_required
def create_movie(request):
  top_movies = TopMovie.objects.filter(user=request.user)
  if request.method == "POST":
    Movie.objects.create(
    nome = request.POST["nome"],
    genero = request.POST["genero"],
    nota = request.POST["nota"],
    link = request.POST["link"],
    filme = TopMovie.objects.get(id=request.POST["filme"]),
    user = request.user
      )
    return redirect(home)
  return render(request, "movies_forms.html", context={"type": "Adicionar", "top_movies": top_movies})


@login_required
def update_movie(request):
  if request.method == "POST":
    Movie.objects.create(
    nome = request.POST["nome"],
    genero = request.POST["genero"],
    nota = request.POST["nota"],
    link = request.POST["link"],
    filme = request.filme,
    user = request.user
      )
    return redirect(home)
  return render(request, "movies_forms.html", context={"type": "Adicionar"})