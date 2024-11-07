from django.urls import path
from PUCMais import views

urlpatterns = [
    path("", views.home, name="home"),
]
