from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Users
from contratantes.models import Contratantes
from posts.models import Posts

class PostTests(TestCase):
    def setUp(self):
        # Configurar o client para as requisições da API
        self.client = APIClient()

        # Criar usuário para autenticação
        self.user = Users.objects.create_user(
            nome='Test User',
            email='testuser@example.com',
            password='testpassword'
        )
        self.user_token = str(RefreshToken.for_user(self.user).access_token)

        # Criar contratante para associar aos posts
        self.contratante = Contratantes.objects.create(
            nome="Contratante A",
            cnpj="12.345.678/0001-90",  # Insira um CNPJ válido
            email="contato@contratante.com"
        )

        # Criar post associado ao usuário e contratante
        self.post = Posts.objects.create(
            titulo="Post de Teste",
            descricao="Descrição do post de teste",
            localizacao="Localização de Teste",
            tipo="Tipo A",
            status="Ativo",
            likes=0,
            deslikes=0,
            user_id=self.user,
        )
        self.post.contratantes.add(self.contratante)

    def test_listar_posts(self):
        """Testa a listagem de posts"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.titulo)

    def test_criar_post(self):
        """Testa a criação de um novo post"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.post(reverse('posts_list'), {
            'titulo': 'Novo Post',
            'descricao': 'Descrição do novo post',
            'localizacao': 'Localização do novo post',
            'tipo': 'Tipo B',
            'status': 'Ativo',
            'likes': 0,
            'deslikes': 0,
            'user_id': self.user.id,
            'contratantes': [self.contratante.id],
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Posts.objects.filter(titulo="Novo Post").exists())

    def test_get_post(self):
        """Testa a consulta de um post específico"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['titulo'], self.post.titulo)

    def test_atualizar_post(self):
        """Testa a atualização de um post existente"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.put(reverse('post_detail', kwargs={'pk': self.post.id}), {
            'titulo': 'Post Atualizado',
            'descricao': 'Descrição atualizada',
            'localizacao': 'Nova localização',
            'tipo': 'Tipo C',
            'status': 'Inativo',
            'likes': 0,
            'deslikes': 0,
            'user_id': self.user.id,
            'contratantes': [self.contratante.id],
        })
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.titulo, 'Post Atualizado')

    def test_deletar_post(self):
        """Testa a exclusão de um post"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.delete(reverse('post_detail', kwargs={'pk': self.post.id}))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Posts.objects.filter(id=self.post.id).exists())

    def test_usuarios_nao_autenticados_nao_podem_criar_ou_editar(self):
        """Testa que usuários não autenticados não podem criar ou editar posts"""
        response = self.client.post(reverse('posts_list'), {
            'titulo': 'Novo Post',
            'descricao': 'Descrição do novo post',
            'localizacao': 'Localização do novo post',
            'tipo': 'Tipo B',
            'status': 'Ativo',
            'likes': 0,
            'deslikes': 0,
            'user_id': self.user.id,
            'contratantes': [self.contratante.id],
        })
        self.assertEqual(response.status_code, 401)

        response = self.client.put(reverse('post_detail', kwargs={'pk': self.post.id}), {
            'titulo': 'Post Editado',
            'descricao': 'Descrição editada',
            'localizacao': 'Localização editada',
            'tipo': 'Tipo D',
            'status': 'Inativo',
            'likes': 0,
            'deslikes': 0,
            'user_id': self.user.id,
            'contratantes': [self.contratante.id],
        })
        self.assertEqual(response.status_code, 401)
