from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    responsaveis = models.ManyToManyField('Responsavel', related_name='alunos', through='AlunoResponsavel')

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class AlunoResponsavel(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    grau_parentesco = models.CharField(max_length=50, blank=True, null=True)
    data_vinculo = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('aluno', 'responsavel')

    def __str__(self):
        return f'{self.responsavel.nome} → {self.aluno.nome}'
    
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
