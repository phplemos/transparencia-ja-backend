from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'nome', 'email', 'senha', 'papel', 'pontos', 'nivel']
