from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Comentarios
from posts.models import Posts
from users.models import Users
from rest_framework_simplejwt.tokens import RefreshToken

class ComentarioTests(TestCase):

    def setUp(self):
        # Criando usuários
        self.usuario = Users.objects.create(nome="Usuario Normal", email="usuario@teste.com", papel="usuario")
        self.gestor = Users.objects.create(nome="Gestor", email="gestor@teste.com", papel="gestor")
        self.administrador = Users.objects.create(nome="Administrador", email="admin@teste.com", papel="administrador")
        
        # Criando um post
        self.post = Posts.objects.create(
            titulo="Post de Teste",
            descricao="Descrição do post",
            localizacao="Localização do post",
            imagem="caminho/para/imagem.jpg",
            tipo="Tipo de Post",
            status="Ativo",
            likes=0,
            deslikes=0,
            user_id=self.usuario
        )
        
        # Criando um comentário
        self.comentario = Comentarios.objects.create(
            texto="Comentário de teste",
            post=self.post,
            user=self.usuario
        )

        # Gerando token para autenticação
        self.gestor_token = RefreshToken.for_user(self.gestor).access_token
        self.administrador_token = RefreshToken.for_user(self.administrador).access_token
        self.usuario_token = RefreshToken.for_user(self.usuario).access_token

        # Usando APIClient
        self.client = APIClient()

    def autenticar(self, token):
        """Método auxiliar para autenticar o cliente."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_deletar_comentario_com_papel_gestor(self):
        self.autenticar(self.gestor_token)
        url = f"/api/comentarios/{self.comentario.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_listar_comentarios(self):
        self.autenticar(self.usuario_token)
        url = f"/api/posts/{self.post.id}/comentarios/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['texto'], "Comentário de teste")

    def test_atualizar_comentario(self):
        self.autenticar(self.usuario_token)
        comentario = Comentarios.objects.create(
            texto="Comentário para atualizar",
            post=self.post,
            user=self.usuario
        )
        url = f"/api/comentarios/{comentario.id}/"
        data = {
            "texto": "Comentário atualizado",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comentario.refresh_from_db()
        self.assertEqual(comentario.texto, "Comentário atualizado")

    def test_deletar_comentario_inexistente(self):
        self.autenticar(self.usuario_token)
        url = "/api/comentarios/999/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
