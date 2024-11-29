from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Course, Topic, Exam, Video, List, Question, Answer, Option, UserCourse, Discipline


def home(request):
  return render(request, 'home.html')


def disciplinas(request):
  disciplinas = Discipline.objects.all()
  return render(request, 'disciplinas.html', {
    'disciplinas': disciplinas,
  })


def Disciplina(request, discipline_name):
  course = Course.objects.filter(discipline__name=discipline_name).all() # Pegar o curso a partir do nome no URL
  try:
    course = course[0]
    usercourse = UserCourse.objects.filter(course = course).filter(user=request.user).all()
  except:
    course = []
    usercourse = []

  return render(request,'Disciplina.html', {
    'course': course,
    'usercourse': usercourse,
  })


def aulas_listas_basic(request, course_name):
  course = Course.objects.filter(name=course_name).all() # Pegar o curso a partir do nome no URL
  topic = Topic.objects.filter(course=course[0].id).all() # Pegar todos os tópicos correlacionados a aquele curso
  videos=Video.objects.filter(topic__in=topic)
  listas=List.objects.filter().all()
  return render(request, "aulas_listas_basic.html",{
    'topics': topic,
    'course': course[0],
    'videos':videos,
    'listas':listas,
  })

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
  provas = Exam.objects.filter(courses=course)
  print(provas)
  return render(request, 'provas_antigas.html', {
    'provas': provas,
    'course_name': course,
  })


@login_required
def perfil(request):
  courses = UserCourse.objects.filter(user=request.user)
  # print(courses)
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
    # return redirect("Disciplina", request.POST["course"])
  return redirect("disciplinas")


@login_required
def removeUserCourse(request):
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


def editUser(request):
  return redirect("home")