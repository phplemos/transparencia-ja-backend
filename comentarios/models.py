from django.db import models
from posts.models import Posts
from users.models import Users  # Importa o modelo customizado

class Comentarios(models.Model):
    texto = models.TextField()
    post = models.ForeignKey(Posts, related_name='comentarios', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    deslikes = models.IntegerField(default=0)

    def __str__(self):
        return f"Comentário de {self.user.nome} em {self.post.titulo}"
