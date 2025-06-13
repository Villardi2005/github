from django.shortcuts import render, redirect
from .models import Professor
from django.contrib import messages
from .forms import AlunoForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


# def cadastro_professor(request):
#     if request.method == 'POST':
#         nome = request.POST.get('nome')
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')

#         if nome and email and senha:
#             if Professor.objects.filter(email=email).exists():
#                 messages.error(request, "Este e-mail já está cadastrado.")
#             else:
#                 Professor.objects.create(nome=nome, email=email, senha=senha)
#                 messages.success(request, "Cadastro realizado com sucesso!")
#                 return redirect('cadastro_professor')
#         else:
#             messages.error(request, "Preencha todos os campos.")
    
#     return render(request, 'cadastroprofessor.html')

# def login_view(request):
#     return render(request, 'login.html')


# def cadastrar_aluno(request):
#     if request.method == 'POST':
#         form = AlunoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('aluno_sucesso')
#     else:
#         form = AlunoForm()
#     return render(request, 'cadastrar_aluno.html', {'form': form})

# def cadastro_responsavel(request):
#     if request.method == 'POST':
#         form = ResponsavelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cadastro_responsavel')
#     else:
#         form = ResponsavelForm()
#     return render(request, 'cadastro/cadastro_responsavel.html', {'form': form})

