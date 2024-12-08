from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "nome", "email", "papel", "pontos", "nivel", "bairro", "rua"]  # Adicionando bairro e rua


class UserCreateSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, min_length=8, error_messages={
        "min_length": "A senha deve ter pelo menos 8 caracteres."
    })

    class Meta:
        model = Users
        fields = ["nome", "email", "papel", "senha", "bairro", "rua"]  # Adicionando bairro e rua

    def validate_email(self, value):
        if Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value

    def create(self, validated_data):
        senha = validated_data.pop("senha")
        user = Users.objects.create_user(
            email=validated_data["email"],
            password=senha,
            nome=validated_data["nome"],
            papel=validated_data.get("papel", "cidadao"),
            bairro=validated_data.get("bairro", ""),
            rua=validated_data.get("rua", "")
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["nome"] = user.nome
        token["papel"] = user.papel
        return token
