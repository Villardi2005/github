from django import forms
from .models import Professor, Aluno, Responsavel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'senha']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'idade', 'matricula']

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = ['nome', 'email', 'senha']

# class UsuarioForm(UserCreationForm):
#     class Meta:
#         model = Usuario
#         fields = ['username', 'password1', 'password2', 'nome_completo', 'telefone']

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']