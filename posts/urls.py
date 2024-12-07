from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsList.as_view(), name='posts_list'),  # Para listar ou criar posts
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),  # Para detalhar, atualizar ou excluir posts
]
