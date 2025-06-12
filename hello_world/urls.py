from django.urls import path
from . import views

urlpatterns = [
    path('cadastroprofessor/', views.cadastro_professor, name='cadastro_professor'),
]
