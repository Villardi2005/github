from django.shortcuts import render, redirect
from .models import Professor
from django.contrib import messages

def cadastro_professor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if nome and email and senha:
            if Professor.objects.filter(email=email).exists():
                messages.error(request, "Este e-mail já está cadastrado.")
            else:
                Professor.objects.create(nome=nome, email=email, senha=senha)
                messages.success(request, "Cadastro realizado com sucesso!")
                return redirect('cadastro_professor')
        else:
            messages.error(request, "Preencha todos os campos.")
    
    return render(request, 'cadastroprofessor.html')

def login_view(request):
    return render(request, 'login.html')

from .forms import AlunoForm

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluno_sucesso')
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_aluno.html', {'form': form})


