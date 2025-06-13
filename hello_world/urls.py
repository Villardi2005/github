from django.urls import path
from evasao import views
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from evasao import views

urlpatterns = [
    # path('cadastroprofessor/', views.cadastro_professor, name='cadastro_professor'),
    # path('admin/', admin.site.urls),
    # path('login/', views.login_view, name='login'),
    # path('cadastro/aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    # path('cadastro/', views.cadastro_responsavel, name='cadastro_responsavel'),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cadastroaluno', views.cadastroaluno, name='cadastroaluno'),
    path('cadastroprofessor', views.cadastroprofessor, name='cadastroprofessor'),
    path('cadastroresponsavel', views.cadastroresponsavel, name='cadastroresponsavel'),
    path("__reload__/", include("django_browser_reload.urls")),
]