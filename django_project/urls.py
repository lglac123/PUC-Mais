from django.contrib import admin
from django.urls import path, include

from django.conf import settings
# from django.conf.urls import url
from django.conf.urls.static import static
# from django.views.static import serve

from app import views

urlpatterns = [
    path("users/signin/", views.createUser),
    path("users/login/", views.loginUser, name = "login"),
    path("users/logout/", views.logoutUser, name = "logout"),
    path("", views.home, name = "home"),
    path("admin/", admin.site.urls),
    path("provas/", views.provas),
    path("aulas/", views.aulas),
    path('perfil/', views.Perfil),
    path('disciplinas/',views.disciplinas),
    path("disciplinas/<str:course_name>",views.Disciplina),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path> .*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         })
#     ]
