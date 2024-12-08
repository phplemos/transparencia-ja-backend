from django.test import TestCase
from users.models import Users
from .models import Notificacao
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class NotificacaoTests(TestCase):
    
    def setUp(self):
        # Criar um usuário para associar à notificação
        self.user = Users.objects.create_user(
            nome="User 1",
            email="user1@example.com",
            password="password123",
            bairro="Centro"
        )

        # Gerar um token de acesso para o usuário
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Criar uma notificação
        self.notificacao_data = {
            "titulo": "Notificação Importante",
            "mensagem": "Esta é uma mensagem de notificação.",
            "todos_usuarios": True,
            "bairros": "",  # Sem bairros específicos
        }

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_criar_notificacao(self):
        response = self.client.post("/api/notificacoes/", self.notificacao_data, format="json")  # Prefixo "api/"
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_listar_notificacoes(self):
        Notificacao.objects.create(
            titulo="Notificação 1",
            mensagem="Mensagem de teste",
            todos_usuarios=True,
        )
        response = self.client.get("/api/notificacoes/")  # Prefixo "api/"
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_notificacao(self):
        notificacao = Notificacao.objects.create(
            titulo="Notificação Inicial",
            mensagem="Mensagem inicial",
            todos_usuarios=True,
        )
        url = f"/api/notificacoes/{notificacao.id}/"  # Prefixo "api/"
        data = {
            "titulo": "Notificação Atualizada",
            "mensagem": "Mensagem atualizada",
            "todos_usuarios": True,
            "bairros": "",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_notificacao(self):
        notificacao = Notificacao.objects.create(
            titulo="Notificação a ser deletada",
            mensagem="Mensagem que será deletada",
            todos_usuarios=True,
        )
        url = f"/api/notificacoes/{notificacao.id}/"  # Prefixo "api/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_usuarios_nao_autenticados_nao_podem_criar_ou_editar(self):
        # Testa que usuários não autenticados não podem criar ou editar notificações
        client = APIClient()
        response = client.post("/api/notificacoes/", self.notificacao_data, format="json")  # Prefixo "api/"
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Tentando editar sem autenticação
        notificacao = Notificacao.objects.create(
            titulo="Notificação Inicial",
            mensagem="Mensagem inicial",
            todos_usuarios=True,
        )
        url = f"/api/notificacoes/{notificacao.id}/"  # Prefixo "api/"
        response = client.put(url, self.notificacao_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

