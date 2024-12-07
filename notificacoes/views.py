from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from users.models import Users
from .models import Notificacao
from .serializers import NotificacaoSerializer

# Para listar e criar notificações
class NotificacaoList(APIView):
    # Método GET: Lista todas as notificações
    def get(self, request):
        notificacoes = Notificacao.objects.all()
        serializer = NotificacaoSerializer(notificacoes, many=True)
        return Response(serializer.data)

    # Método POST: Cria uma nova notificação
    def post(self, request):
        serializer = NotificacaoSerializer(data=request.data)
        if serializer.is_valid():
            notificacao = serializer.save()
            # Lógica para associar usuários
            todos_usuarios = request.data.get("todos_usuarios", False)
            bairros = request.data.get("bairros")

            if todos_usuarios:
                usuarios = Users.objects.all()
            elif bairros:
                lista_bairros = [b.strip() for b in bairros.split(",")]
                usuarios = Users.objects.filter(bairro__in=lista_bairros)
            else:
                usuarios = []

            notificacao.usuarios.add(*usuarios)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Para obter, atualizar e excluir uma notificação específica
class NotificacaoDetail(APIView):
    # Método auxiliar para buscar uma notificação pelo ID
    def get_object(self, pk):
        try:
            return Notificacao.objects.get(pk=pk)
        except Notificacao.DoesNotExist:
            raise NotFound("Notificação não encontrada")

    # Método GET: Detalha uma notificação
    def get(self, request, pk):
        notificacao = self.get_object(pk)
        serializer = NotificacaoSerializer(notificacao)
        return Response(serializer.data)

    # Método PUT: Atualiza uma notificação
    def put(self, request, pk):
        notificacao = self.get_object(pk)
        serializer = NotificacaoSerializer(notificacao, data=request.data)
        if serializer.is_valid():
            notificacao = serializer.save()
            # Atualizar os usuários associados
            todos_usuarios = request.data.get("todos_usuarios", False)
            bairros = request.data.get("bairros")

            if todos_usuarios:
                usuarios = Users.objects.all()
            elif bairros:
                lista_bairros = [b.strip() for b in bairros.split(",")]
                usuarios = Users.objects.filter(bairro__in=lista_bairros)
            else:
                usuarios = []

            notificacao.usuarios.set(usuarios)  # Atualiza os usuários associados
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método DELETE: Exclui uma notificação
    def delete(self, request, pk):
        notificacao = self.get_object(pk)
        notificacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
