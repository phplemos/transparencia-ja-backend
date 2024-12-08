from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Users


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = Users.objects.create_user(
            nome="Test User",
            email="testuser@example.com",
            password="testpassword",
            bairro="Centro",
            rua="Rua Principal"
        )
        self.user_token = str(RefreshToken.for_user(self.user).access_token)

    def test_criar_usuario(self):
        # Configura o cabeçalho de autorização com o token de um usuário autenticado
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')

        response = self.client.post(reverse("users-list-create"), {
            "nome": "Novo Usuário",
            "email": "novousuario@example.com",
            "senha": "senha123"
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Users.objects.filter(email="novousuario@example.com").exists())

    def test_criar_usuario_com_geolocalizacao(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        
        response = self.client.post(reverse("users-list-create"), {
            "nome": "Novo Usuário",
            "email": "novousuario@example.com",
            "senha": "senha123",
            "bairro": "Jardim das Flores",  # Novo campo
            "rua": "Rua das Flores"  # Novo campo
        })
        
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Users.objects.filter(email="novousuario@example.com").exists())
        novo_usuario = Users.objects.get(email="novousuario@example.com")
        self.assertEqual(novo_usuario.bairro, "Jardim das Flores")
        self.assertEqual(novo_usuario.rua, "Rua das Flores")
        
    def test_usuario_nao_autenticado(self):
        # Teste para criação de usuário sem autenticação
        response = self.client.get(reverse("users-list-create"))
        # Verifica se a resposta é 401 (não autenticado)
        self.assertEqual(response.status_code, 401)

    def test_permissao_acesso_gerenciamento(self):
        # Teste para usuário autenticado editar o próprio perfil
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        response = self.client.patch(reverse("user-detail", kwargs={"pk": self.user.id}), {
            "nome": "User Editado"
        })
        # Verifica se a edição foi bem-sucedida
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()  # Atualiza o usuário após a edição
        self.assertEqual(self.user.nome, "User Editado")

    def test_usuario_nao_autenticado_nao_pode_editar(self):
        # Teste para tentativa de edição sem autenticação
        response = self.client.patch(reverse("user-detail", kwargs={"pk": self.user.id}), {
            "nome": "Tentativa de Edição"
        })
        # Verifica se a resposta é 401 (não autenticado)
        self.assertEqual(response.status_code, 401)

    def test_usuarios_nao_autenticados_nao_podem_criar_ou_editar(self):
        # Remover autenticação
        self.client.credentials()

        # Teste para criação de usuário (usuário não autenticado)
        response = self.client.post(reverse("users-list-create"), {
            "nome": "Novo Usuário",
            "email": "novousuario@example.com",
            "senha": "senha123"  # Usando 'senha' conforme o serializer
        })
        # Verifica se a resposta é 401 (não autenticado)
        self.assertEqual(response.status_code, 401)

        # Teste para edição de usuário (usuário não autenticado)
        response = self.client.patch(reverse("user-detail", kwargs={"pk": self.user.id}), {
            "nome": "Tentativa de Edição"
        })
        # Verifica se a resposta é 401 (não autenticado)
        self.assertEqual(response.status_code, 401)

    def test_listagem_de_usuarios_para_usuario_autenticado(self):
        # Testa a listagem de usuários para usuário autenticado
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        response = self.client.get(reverse("users-list-create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.nome)

    def test_listagem_de_usuarios_para_usuario_nao_autenticado(self):
        # Testa a listagem de usuários para usuário não autenticado
        self.client.credentials()  # Remover autenticação
        response = self.client.get(reverse("users-list-create"))
        # Verifica se a resposta é 401 (não autenticado)
        self.assertEqual(response.status_code, 401)
