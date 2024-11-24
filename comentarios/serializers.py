from rest_framework import serializers
from .models import Comentarios

class ComentariosSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')
    post_titulo = serializers.ReadOnlyField(source='post.titulo')

    class Meta:
        model = Comentarios
        fields = ['id', 'texto', 'post', 'post_titulo', 'user', 'user_nome', 'data_criacao', 'likes', 'deslikes']
