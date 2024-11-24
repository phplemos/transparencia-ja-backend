from rest_framework import serializers
from .models import Posts
from contratantes.models import Contratantes
from contratantes.serializers import ContratantesSerializer
from comentarios.serializers import ComentariosSerializer

class PostsSerializer(serializers.ModelSerializer):
    contratantes = ContratantesSerializer(many=True)
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
        for contratante_data in contratantes_data:
            contratante, _ = Contratantes.objects.get_or_create(**contratante_data)
            post.contratantes.add(contratante)
        return post

    # Atualizar posts e seus contratantes
    def update(self, instance, validated_data):
        contratantes_data = validated_data.pop('contratantes', [])
        instance = super().update(instance, validated_data)

        # Atualizar contratantes relacionados
        instance.contratantes.clear()
        for contratante_data in contratantes_data:
            contratante, _ = Contratantes.objects.get_or_create(**contratante_data)
            instance.contratantes.add(contratante)
        return instance
