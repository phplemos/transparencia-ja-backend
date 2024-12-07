from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "nome", "email", "papel", "pontos", "nivel"]


class UserCreateSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)  # Usar "senha" para entrada

    class Meta:
        model = Users
        fields = ["nome", "email", "papel", "senha"]

    def create(self, validated_data):
        # Passar a senha como argumento
        senha = validated_data.pop("senha")
        return Users.objects.create_user(
            email=validated_data["email"],
            senha=senha,  # Define o campo "senha"
            nome=validated_data["nome"],
            papel=validated_data.get("papel", "cidadao"),
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adiciona informações personalizadas ao token
        token["nome"] = user.nome
        token["papel"] = user.papel
        return token
