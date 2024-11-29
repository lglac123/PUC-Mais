from django.contrib import admin
from django.urls import path, include

from django.conf import settings
# from django.conf.urls import url
from django.conf.urls.static import static
# from django.views.static import serve

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/signin/", views.createUser),
    path("users/login/", views.loginUser, name = "login"),
    path("users/logout/", views.logoutUser, name = "logout"),
    path("users/edit/", views.editUser),
    path("", views.home, name = "home"),
    # path("aulas/", views.aulas),
    path('perfil/', views.perfil, name="perfil"),
    path('disciplinas/', views.disciplinas, name="disciplinas"),
    path("disciplinas/<str:discipline_name>", views.Disciplina, name="Disciplina"),
    path("disciplinas/<str:course_name>/aulas&listas/", views.aulas_listas_basic),
    path("disciplinas/<str:course_name>/aulas&listas/<str:topic_name>/",views.listas),
    path("disciplinas/<str:course_name>/provas/", views.provas),
    path("userCourse/create/", views.createUserCourse),
    path("userCourse/delete/", views.removeUserCourse),
    path("userCourse/favorite/", views.favoriteUserCourseChange),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)