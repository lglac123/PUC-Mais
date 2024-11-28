from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Course, Topic, Exam, Video, List, Question, Answer, Option, UserCourse
from .forms import BuscaAno

def home(request):
  return render(request, 'home.html')


def disciplinas(request):
  courses = Course.objects.all()
  return render(request, 'disciplinas.html', {
    'courses': courses,
  })


def Disciplina(request, course_name):
  course = Course.objects.get(name=course_name) # Pegar o curso a partir do nome no URL
  print(course)
  return render(request,'Disciplina.html', {
    'course': course,
  })


def aulas_listas_basic(request, course_name):
  course = Course.objects.filter(name=course_name).all() # Pegar o curso a partir do nome no URL
  topic = Topic.objects.filter(course=course[0].id).all() # Pegar todos os tópicos correlacionados a aquele curso
  videos=Video.objects.filter(topic__in=topic)
  return render(request, "aulas_listas_basic.html",{
    'topics': topic,
    'course': course[0],
    'videos':videos,
  })


@login_required
def provas(request, course_name):
  course = Course.objects.get(name=course_name)
  provas = Exam.objects.filter(courses=course)
  return render(request, 'provas_antigas.html', {
    'provas': provas,
    'course_name': course,
  })

@login_required
def BuscaAnoProva(request):
    # Inicializa o formulário com os dados recebidos pelo GET
    formulario = BuscaAno(request.GET or None)
    resultado = None  # Inicializa o resultado como vazio

    if formulario.is_valid():
        # Obtém o dado do campo 'nome' do formulário
        nome = formulario.cleaned_data.get('nome')  # Usa .get() para evitar KeyError
        if nome:  # Apenas filtre se um nome válido foi fornecido
            resultado = Exam.objects.filter(name__icontains=nome)

    # Renderiza a página com o formulário e os resultados
    return render(
        request,
        'BuscaAno.html',
        {'formulario': formulario, 'resultado': resultado}
    )
@login_required
def perfil(request):
  courses = UserCourse.objects.filter(user=request.user)
  print(courses)
  return render(request,'perfil.html', {
    'userCourse': courses,
  })


@login_required
def createUserCourse(request):
  if request.method == "POST":
    userCourse_new = UserCourse()
    userCourse_new.course = Course.objects.get(name = request.POST["course"])
    userCourse_new.user = request.user
    userCourse_new.status = 0

    userCourse_new.save()
    print(userCourse_new)
    return redirect("Disciplina", request.POST["course"])
  return redirect("disciplinas")


def removeUserCourse(request):
  if request.method == "POST":
    usercourse = UserCourse.objects.get(id = request.POST["userCourseId"])
    usercourse.delete()
    return redirect("home")
  
  usercourse = UserCourse.objects.get(id = request.GET.get("courseId"))
  print(usercourse)
  return render(request, "deleteUserCourse.html", {
    'userCourse': usercourse,
  })

def favoriteUserCourseChange(request):

  usercourse = UserCourse.objects.get(id = request.POST["courseId"])


  if usercourse.favorite == 0:
    usercourse.favorite = 1
  else:
    usercourse.favorite = 0
  usercourse.save()

  return redirect("perfil")  


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
  print("ver se esta chamando a view")  
  if request.method == "POST":  
    print("ver se esta pegando o metodo")
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