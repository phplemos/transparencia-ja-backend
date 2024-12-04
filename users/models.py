from django.db import models

class Users(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    papel = models.CharField(max_length=200, default='cidadao')  # Valor padrão 'cidadao'
    pontos = models.FloatField(default=0.0)  # Valor padrão 0.0
    nivel = models.IntegerField(default=1)  # Valor padrão 1

    def __str__(self):
        return self.nome