from rest_framework import serializers
from .models import Posts  # Importando o modelo Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = [
            'id', 
            'titulo', 
            'descricao',
            'localizacao',
            'imagem',
            'tipo',
            'status',
            'pdf',
            'likes',
            'deslikes',
            'comentarios',
            'user_id',
            'contratante',
        ]
