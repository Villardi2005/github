from django.db import models
from django.contrib.auth.models import AbstractUser

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username
        
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)  # Em produção, use hash e autenticação segura

    def __str__(self):
        return self.nome
