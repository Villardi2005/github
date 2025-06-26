from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()  # <-- esse campo precisa existir

    def __str__(self):
        return self.nome
