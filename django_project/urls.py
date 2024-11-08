from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path("users/signin/", views.createUser),
    path("users/login/", views.loginUser, name = "login"),
    path("users/logout/", views.logoutUser, name = "logout"),
    path("", views.home, name = "home"),
    path("admin/", admin.site.urls),
    path("provas/", views.provas),
    path("aulas/", views.aulas),
    path('disciplinas/',views.disciplinas),
]
