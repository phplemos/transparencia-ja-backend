from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Users
from .serializers import UserSerializer, UserCreateSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UsersListCreateAPIView(APIView):
    """
    GET: Lista todos os usuários (apenas para usuários autenticados).
    POST: Cria um novo usuário (somente para usuários autenticados).
    """
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]  # Mudando para IsAuthenticated
        return [IsAuthenticated()]

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Retornar dados públicos
            public_serializer = UserSerializer(user)
            return Response(public_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    """
    GET, PATCH, DELETE para um único usuário (restrito ao proprietário).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        if not self._is_owner(request, pk):
            return Response({"detail": "Você não tem permissão para acessar este recurso."}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = Users.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, *args, **kwargs):
        if not self._is_owner(request, pk):
            return Response({"detail": "Você não tem permissão para modificar este recurso."}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = Users.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        if not self._is_owner(request, pk):
            return Response({"detail": "Você não tem permissão para excluir este recurso."}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = Users.objects.get(pk=pk)
            user.delete()
            return Response({"detail": "Usuário excluído com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def _is_owner(self, request, pk):
        return request.user.id == pk


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
