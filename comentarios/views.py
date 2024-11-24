from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Comentarios
from .serializers import ComentariosSerializer
from posts.models import Posts
from users.models import Users

# Listar todos os comentários de um post específico
@api_view(['GET'])
def listar_comentarios(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)  # Busca o post pelo ID
        comentarios = post.comentarios.all()  # Recupera todos os comentários associados a este post
    except Posts.DoesNotExist:
        return Response({'error': 'Post não encontrado'}, status=404)  # Retorna erro se o post não for encontrado
    
    serializer = ComentariosSerializer(comentarios, many=True)
    return Response({'comentarios': serializer.data})

@api_view(['POST'])
def criar_comentario(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)  # Busca o post pelo ID
    except Posts.DoesNotExist:
        return Response({'error': 'Post não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user = Users.objects.get(id=request.data.get('user'))  # Busca o usuário pelo ID enviado
    except Users.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    # Adiciona o post e o usuário ao comentário
    data = request.data.copy()
    data['post'] = post.id
    data['user'] = user.id

    serializer = ComentariosSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Visualizar um comentário específico
@api_view(['GET'])
def visualizar_comentario(request, comentario_id):
    try:
        comentario = Comentarios.objects.get(id=comentario_id)  # Busca o comentário pelo ID
    except Comentarios.DoesNotExist:
        return Response({'error': 'Comentário não encontrado'}, status=404)  # Caso o comentário não seja encontrado
    
    serializer = ComentariosSerializer(comentario)
    return Response({'comentario': serializer.data})

# Curtir um comentário
@api_view(['POST'])
def curtir_comentario(request, comentario_id):
    try:
        comentario = Comentarios.objects.get(id=comentario_id)
    except Comentarios.DoesNotExist:
        return Response({'error': 'Comentário não encontrado'}, status=404)

    comentario.likes += 1  # Incrementa o número de likes
    comentario.save()  # Salva o comentário atualizado
    return Response({'message': 'Comentário curtido', 'likes': comentario.likes})

# Descurtir um comentário
@api_view(['POST'])
def descurtir_comentario(request, comentario_id):
    try:
        comentario = Comentarios.objects.get(id=comentario_id)
    except Comentarios.DoesNotExist:
        return Response({'error': 'Comentário não encontrado'}, status=404)

    comentario.deslikes += 1  # Incrementa o número de deslikes
    comentario.save()  # Salva o comentário atualizado
    return Response({'message': 'Comentário descurtido', 'deslikes': comentario.deslikes})
