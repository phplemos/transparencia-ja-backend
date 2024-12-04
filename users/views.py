from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class UsersAPIView(APIView):
    """
    API para gerenciar usuários.
    """

    def get(self, request, *args, **kwargs):
        """
        Método GET para listar todos os usuários.
        """
        users = Users.objects.all()  # Busca todos os usuários no banco de dados
        serializer = UserSerializer(users, many=True)  # Serializa a lista de usuários
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Método POST para criar um novo usuário.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        Método PUT para atualizar um usuário existente.
        """
        user_id = kwargs.get('pk')
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Método DELETE para excluir um usuário existente.
        """
        user_id = kwargs.get('pk')
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message": "Usuário deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Customização do TokenObtainPairView para retornar tokens JWT.
    """
    pass  # Se você precisar customizar a resposta, pode fazer isso aqui
