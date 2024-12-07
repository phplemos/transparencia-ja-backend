from rest_framework import serializers
from .models import Posts
from contratantes.models import Contratantes
from contratantes.serializers import ContratantesSerializer
from comentarios.serializers import ComentariosSerializer

class PostsSerializer(serializers.ModelSerializer):
    contratantes = serializers.PrimaryKeyRelatedField(queryset=Contratantes.objects.all(), many=True)
    comentarios = ComentariosSerializer(many=True, read_only=True)

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
            'contratantes',
        ]

    # Criar novos posts com contratantes
    def create(self, validated_data):
        contratantes_data = validated_data.pop('contratantes', [])
        post = Posts.objects.create(**validated_data)
        post.contratantes.set(contratantes_data)  # Associa os contratantes com base nos IDs
        return post

    # Atualizar posts e seus contratantes
    def update(self, instance, validated_data):
        contratantes_data = validated_data.pop('contratantes', [])
        instance = super().update(instance, validated_data)

        # Atualizar contratantes relacionados
        instance.contratantes.set(contratantes_data)  # Atualiza com os IDs dos contratantes
        return instance
