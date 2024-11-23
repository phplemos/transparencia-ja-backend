from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UserSerializer  # Alterado para UserSerializer

class UsersAPIView(APIView):
    """
    API para gerenciar usuários.
    """

    # Método GET para listar todos os usuários
    def get(self, request, *args, **kwargs):
        users = Users.objects.all()  # Busca todos os usuários no banco de dados
        serializer = UserSerializer(users, many=True)  # Alterado para UserSerializer
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Método POST para criar um novo usuário
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)  # Alterado para UserSerializer
        if serializer.is_valid():  # Verifica se os dados são válidos
            serializer.save()  # Salva o usuário no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método PUT para atualizar um usuário existente
    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')  # Obtém o ID do usuário a ser atualizado
        try:
            user = Users.objects.get(id=user_id)  # Busca o usuário no banco de dados
        except Users.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)  # Alterado para UserSerializer
        if serializer.is_valid():  # Verifica se os dados são válidos
            serializer.save()  # Atualiza o usuário no banco de dados
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método DELETE para excluir um usuário existente
    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')  # Obtém o ID do usuário a ser deletado
        try:
            user = Users.objects.get(id=user_id)  # Busca o usuário no banco de dados
        except Users.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        user.delete()  # Deleta o usuário do banco de dados
        return Response({"message": "Usuário deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
