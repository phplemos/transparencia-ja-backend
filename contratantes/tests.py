from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Contratantes
from users.models import Users  # Importando o modelo de usuário (presumindo que o modelo seja 'Users')
from rest_framework_simplejwt.tokens import RefreshToken

class ContratanteTests(TestCase):

    def setUp(self):
        self.user = Users.objects.create_user(
            nome="User Teste",
            email="user@teste.com",
            password="password123"
        )

        # Criar um cliente API
        self.client = APIClient()

        # Gerar token para o usuário
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        # Definir o token no cabeçalho Authorization para as requisições
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Criar dados de um contratante para testes
        self.contratante_data = {
            "nome": "Contratante Teste",
            "cnpj": "12.345.678/0001-99",
            "email": "teste@contratante.com"
        }

    def test_criar_contratante(self):
        # Testa a criação de um contratante
        response = self.client.post("/api/contratantes/", self.contratante_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contratantes.objects.count(), 1)
        self.assertEqual(Contratantes.objects.get().nome, "Contratante Teste")

    def test_listar_contratantes(self):
        # Testa a listagem de contratantes
        Contratantes.objects.create(**self.contratante_data)
        response = self.client.get("/api/contratantes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], "Contratante Teste")

    def test_atualizar_contratante(self):
        # Testa a atualização de um contratante
        contratante = Contratantes.objects.create(**self.contratante_data)
        url = f"/api/contratantes/{contratante.id}/"
        data = {
            "nome": "Contratante Atualizado",
            "cnpj": "98.765.432/0001-00",
            "email": "atualizado@contratante.com"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        contratante.refresh_from_db()
        self.assertEqual(contratante.nome, "Contratante Atualizado")

    def test_deletar_contratante(self):
        # Testa a exclusão de um contratante
        contratante = Contratantes.objects.create(**self.contratante_data)
        url = f"/api/contratantes/{contratante.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contratantes.objects.count(), 0)

    def test_obter_contratante_inexistente(self):
        # Testa tentativa de acessar um contratante inexistente
        url = "/api/contratantes/999/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_atualizar_contratante_inexistente(self):
        # Testa tentativa de atualizar um contratante inexistente
        url = "/api/contratantes/999/"
        data = {
            "nome": "Contratante Inexistente",
            "cnpj": "98.765.432/0001-00",
            "email": "inexistente@contratante.com"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_deletar_contratante_inexistente(self):
        # Testa tentativa de excluir um contratante inexistente
        url = "/api/contratantes/999/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
