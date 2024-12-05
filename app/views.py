from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Course, Topic, Exam, Video, List, Question, Answer, Option, UserCourse, Discipline
from .forms import BuscaAno

def home(request):
  return render(request, 'home.html')


def disciplinas(request):
  disciplinas = Discipline.objects.all()
  return render(request, 'disciplinas.html', {
    'disciplinas': disciplinas,
  })


def Disciplina(request, discipline_name):
  try: # Tô nem aí para beleza do código
    course_basic = Course.objects.get(discipline__name = discipline_name, isadvanced = False)
  except:
    course_basic = None

  try:
    course_advanced = Course.objects.get(discipline__name = discipline_name, isadvanced = True)
  except:
    course_advanced = None

  usercourse_basic = False
  usercourse_advanced = False
  if request.user.is_authenticated:
    try:
      usercourse_basic = UserCourse.objects.filter(course = course_basic).filter(user=request.user).all()
    except:
      print("YAY")

    try:
      usercourse_advanced = UserCourse.objects.filter(course = course_advanced).filter(user = request.user).all()
    except:
      print("YAY")
    print(usercourse_basic, usercourse_advanced)

  return render(request,'Disciplina.html', {
    'discipline_name': discipline_name,
    'course_basic': course_basic,
    'course_advanced': course_advanced,
    'usercourse_basic': usercourse_basic,
    'usercourse_advanced': usercourse_advanced,
  })


def aulas_listas_basic(request, discipline_name):
  discipline = get_object_or_404(Discipline, name = discipline_name) # Discipline.objects.get(name = discipline_name)
  courses = Course.objects.filter(discipline__name = discipline_name).all() # Pegar os cursos a partir do nome no URL
  # E se for vazio?
  topic = Topic.objects.filter(course__in=courses).all() # Pegar todos os tópicos correlacionados a aquele curso
  videos=Video.objects.filter(topic__in=topic)
  listas=List.objects.filter().all()
  return render(request, "aulas_listas_basic.html",{
    'topics': topic,
    'discipline': discipline,
    'videos':videos,
    'listas':listas,
  })

@login_required
def BuscaAnoProva(request):
    # Inicializa o formulário com os dados recebidos pelo GET
    formulario = BuscaAno(request.GET or None)
    resultado = None  # Inicializa o resultado como vazio

    if formulario.is_valid():
        nome = formulario.cleaned_data.get('nome')  
        if nome:  
            resultado = Exam.objects.filter(name__icontains=nome)
    return render(
        request,
        'BuscaProva.html',
        {'formulario': formulario, 'resultado': resultado}
    )

def listas(request, course_name, topic_name):
  course = Course.objects.filter(name=course_name).all()  # Pegar o curso a partir do nome no URL
  try:
    topic = Topic.objects.get(name=topic_name)  # Pega o único tópico pelo nome
  except Topic.DoesNotExist:
    topic = None  # Se não encontrar, o tópico será None (ou você pode exibir uma mensagem de erro no template)
  
  lista = List.objects.filter().all()  # Pegar a lista
  questions = Question.objects.filter(topic=topic)  # Filtrar questões para o tópico
  
  return render(request, "listas.html", {
      'topic': topic,  # Passando o tópico para o template
      'course': course[0] if course else None,  # Verifique se o curso existe
      'lista': lista,
      'questions': questions,
  })


@login_required
def provas(request, course_name):
  course = Course.objects.get(name=course_name)
  # E se não existir?
  provas = Exam.objects.filter(courses=course)
  print(provas)
  return render(request, 'provas_antigas.html', {
    'provas': provas,
    'course_name': course,
  })


@login_required
def perfil(request):
  courses = UserCourse.objects.filter(user=request.user)
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
  return redirect("Disciplina", discipline_name = request.POST["discipline_name"])


@login_required
def removeUserCourse(request):
  # E se não for post?
  if request.method == "POST":
    usercourse = UserCourse.objects.get(id = request.POST["userCourseId"])
    usercourse.delete()
    return redirect("perfil")
  
  usercourse = UserCourse.objects.get(id = request.GET.get("courseId"))
  print(usercourse)
  return render(request, "deleteUserCourse.html", {
    'userCourse': usercourse,
  })


def favoriteUserCourseChange(request):
  if request.method == "POST":
    print(request.POST["courseId"])
    usercourse = UserCourse.objects.get(id = request.POST["courseId"])
    usercourse.favorite = (usercourse + 1) % 2
    # if usercourse.favorite == 0:
    #   usercourse.favorite = 1
    # else:
    #   usercourse.favorite = 0
    usercourse.save()

  return redirect("perfil")  


def FAQ(request):
  return render(request,'FAQ.html')

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


def editUser(request):
  return redirect("home")