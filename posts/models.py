from django.db import models
from contratantes.models import Contratantes  # Importe o modelo Contratantes

class Posts(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=200)
    imagem = models.CharField(max_length=200, default="")
    tipo = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
    likes = models.IntegerField()
    deslikes = models.IntegerField()
    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    contratantes = models.ManyToManyField(Contratantes, related_name="posts")

    def __str__(self):  
        return self.titulo
