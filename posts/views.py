from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Posts
from .serializers import PostsSerializer
from rest_framework.permissions import IsAuthenticated

class PostsList(APIView):
   permission_classes = [IsAuthenticated]
    # Método GET: Lista todos os posts
   def get(self, request):
    # Adicionar filtros por query params
    tipo = request.query_params.get('tipo')
    status = request.query_params.get('status')
    
    # Filtrar conforme os parâmetros, se fornecidos
    posts = Posts.objects.all()
    if tipo:
        posts = posts.filter(tipo=tipo)
    if status:
        posts = posts.filter(status=status)

    serializer = PostsSerializer(posts, many=True)
    return Response(serializer.data)


    # Método POST: Cria um novo post
   def post(self, request):
    serializer = PostsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)  # Exibe os erros de validação no console
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    # Método GET: Retorna um único post pelo ID
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise NotFound("Post not found")

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    # Método PUT: Atualiza um post existente
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método DELETE: Deleta um post existente
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
