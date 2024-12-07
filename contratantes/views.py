from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Contratantes
from .serializers import ContratantesSerializer

# Para listar e criar contratantes
class ContratanteList(APIView):
    # Método GET: Lista todos os contratantes
    def get(self, request):
        contratantes = Contratantes.objects.all()
        serializer = ContratantesSerializer(contratantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Método POST: Cria um novo contratante
    def post(self, request):
        serializer = ContratantesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Para obter, atualizar e excluir um contratante específico
class ContratanteDetail(APIView):
    # Método auxiliar para buscar um contratante pelo ID
    def get_object(self, id):
        try:
            return Contratantes.objects.get(id=id)
        except Contratantes.DoesNotExist:
            raise NotFound("Contratante não encontrado")

    # Método GET: Detalha um contratante
    def get(self, request, id):
        contratante = self.get_object(id)
        serializer = ContratantesSerializer(contratante)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Método PUT: Atualiza um contratante
    def put(self, request, id):
        contratante = self.get_object(id)
        serializer = ContratantesSerializer(contratante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método DELETE: Exclui um contratante
    def delete(self, request, id):
        contratante = self.get_object(id)
        contratante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
