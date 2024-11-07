from django.contrib import admin
from django.urls import path, include
from PUCMais import views

urlpatterns = [
    path("users/signin/", views.createUser),
    path("users/login/", views.loginUser, name = "login"),
    path("users/logout/", views.logoutUser, name = "logout"),
    path("", views.home, name = "home"),
    path("admin/", admin.site.urls),
    path("top_movie/new", views.create_top_movie),
    path("top_movie/update/<id>", views.update_top_movie),
    path("top_movie/delete/<id>", views.delete_top_movie),
    path("movie/new", views.create_movie),
    path("provas/", views.provas),
    path("aulas/", views.aulas),
]
