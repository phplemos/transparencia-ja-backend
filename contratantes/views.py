from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contratantes
from .serializers import ContratantesSerializer

@api_view(['GET'])
def listar_contratantes(request):
    # Recupera todos os contratantes do banco de dados
    contratantes = Contratantes.objects.all()
    serializer = ContratantesSerializer(contratantes, many=True)
    return Response({'contratantes': serializer.data})

@api_view(['POST'])
def criar_contratante(request):
    if request.method == 'POST':
        serializer = ContratantesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva o novo contratante no banco de dados
            return Response(serializer.data, status=201)  # Retorna os dados criados com status 201
        return Response(serializer.errors, status=400)  # Caso haja erro na validação

@api_view(['GET'])
def visualizar_contratante(request, id):
    try:
        contratante = Contratantes.objects.get(id=id)  # Busca o contratante pelo id
    except Contratantes.DoesNotExist:
        return Response({'error': 'Contratante não encontrado'}, status=404)  # Retorna erro se não encontrar
    serializer = ContratantesSerializer(contratante)
    return Response({'contratante': serializer.data})
