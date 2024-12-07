from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Comentarios
from .serializers import ComentariosSerializer
from posts.models import Posts
from users.models import Users

# Listar e criar comentários de um post específico
class ComentariosList(APIView):
    def get(self, request, post_id):
        try:
            post = Posts.objects.get(id=post_id)  # Busca o post pelo ID
        except Posts.DoesNotExist:
            raise NotFound("Post não encontrado")
        
        comentarios = post.comentarios.all()  # Recupera os comentários associados ao post
        serializer = ComentariosSerializer(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        try:
            post = Posts.objects.get(id=post_id)  # Busca o post pelo ID
        except Posts.DoesNotExist:
            raise NotFound("Post não encontrado")
        
        try:
            user = Users.objects.get(id=request.data.get('user'))  # Busca o usuário pelo ID
        except Users.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        data['post'] = post.id
        data['user'] = user.id

        serializer = ComentariosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Operações de CRUD para um comentário específico
class ComentarioDetail(APIView):
    def get_object(self, comentario_id):
        try:
            return Comentarios.objects.get(id=comentario_id)
        except Comentarios.DoesNotExist:
            raise NotFound("Comentário não encontrado")

    # Visualizar um comentário específico
    def get(self, request, comentario_id):
        comentario = self.get_object(comentario_id)
        serializer = ComentariosSerializer(comentario)
        return Response(serializer.data)

    # Atualizar um comentário específico
    def put(self, request, comentario_id):
        comentario = self.get_object(comentario_id)
        serializer = ComentariosSerializer(comentario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deletar um comentário específico
    def delete(self, request, comentario_id):
        comentario = self.get_object(comentario_id)
        comentario.delete()
        return Response({'message': 'Comentário deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)

# Curtir ou descurtir um comentário específico
class ComentarioCurtir(APIView):
    def get_object(self, comentario_id):
        try:
            return Comentarios.objects.get(id=comentario_id)
        except Comentarios.DoesNotExist:
            raise NotFound("Comentário não encontrado")

    def post(self, request, comentario_id, action):
        comentario = self.get_object(comentario_id)

        if action == "curtir":
            comentario.likes += 1  # Incrementa os likes
        elif action == "descurtir":
            comentario.deslikes += 1  # Incrementa os deslikes
        else:
            return Response({'error': 'Ação inválida'}, status=status.HTTP_400_BAD_REQUEST)
        
        comentario.save()
        return Response({
            'message': f"Comentário {'curtido' if action == 'curtir' else 'descurtido'} com sucesso",
            'likes': comentario.likes,
            'deslikes': comentario.deslikes
        })
