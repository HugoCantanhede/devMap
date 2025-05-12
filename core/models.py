from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Categoria de habilidades: Frontend, Backend, Banco de Dados, etc
class CategoriaHabilidade(models.Model):
    nome = models.CharField(max_length=100)  # Antes: name

    def __str__(self):
        return self.nome

# Uma habilidade individual (React, Django, PostgreSQL, etc)
class Habilidade(models.Model):
    nome = models.CharField(max_length=100)  # Antes: name
    categoria = models.ForeignKey(CategoriaHabilidade, on_delete=models.CASCADE)  # Antes: category

    def __str__(self):
        return self.nome

# Relação entre o usuário e suas habilidades
class HabilidadeUsuario(models.Model):
    NIVEL_CHOICES = [
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Antes: user
    habilidade = models.ForeignKey(Habilidade, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    def __str__(self):
        return f"{self.usuario.username} - {self.habilidade.nome} ({self.get_nivel_display()})"

