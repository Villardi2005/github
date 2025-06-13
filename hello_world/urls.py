from django.urls import path
from evasao import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('cadastroprofessor/', views.cadastro_professor, name='cadastro_professor'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('cadastro/aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastro/', views.cadastro_responsavel, name='cadastro_responsavel'),
]
