from django.db import models
from users.models import Users  # Ajuste o caminho se necessário

class Notificacao(models.Model):
    titulo = models.CharField(max_length=200)  # Título da notificação
    mensagem = models.TextField()  # Corpo da mensagem
    usuarios = models.ManyToManyField(Users, blank=True, related_name="notificacoes")  
    bairros = models.TextField(blank=True, null=True)  # Bairros como texto delimitado por vírgulas
    todos_usuarios = models.BooleanField(default=False)  # Indica se a notificação é para todos
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data e hora da criação

    def __str__(self):
        return f"{self.titulo} - Criado em {self.data_criacao.strftime('%Y-%m-%d %H:%M:%S')}"
