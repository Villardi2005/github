from django.shortcuts import render, redirect
from .models import Aluno
from django.contrib import messages
from .forms import AlunoForm

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def cadastroprofessor(request):
    return render(request, 'cadastroprofessor.html')

def cadastroresponsavel(request):
    return render(request, 'cadastroresponsavel.html')

def painel_responsavel(request):
    return render(request, 'painel/painel_responsavel.html')

def minhas_metas(request):
    # Aqui você pode passar os dados reais do aluno se quiser
    return render(request, 'painel/minhas_metas.html')

def painel_professor(request):
    return render(request, 'painel/painel_professor.html')

def cadastroaluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_concluido')  # você pode criar essa página depois
    else:
        form = AlunoForm()

    return render(request, 'cadastroaluno.html', {'form': form})


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

