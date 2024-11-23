from django.db import models

class Posts(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=200)
    imagem = models.CharField(max_length=200, default="")  # Correção no valor padrão
    tipo = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)  # Campo para armazenar o PDF
    likes = models.IntegerField()
    deslikes = models.IntegerField()
    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)  # Relacionamento com o modelo Users

    def __str__(self):  
        return self.titulo  
