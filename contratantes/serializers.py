from rest_framework import serializers
from .models import Contratantes

class ContratantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratantes
        fields = ['id', 'nome', 'cnpj', 'email']
