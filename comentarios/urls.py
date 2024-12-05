from django.urls import path
from .views import ComentariosList, ComentarioDetail, ComentarioCurtir

urlpatterns = [
    # Listar e criar comentários relacionados a um post
    path('posts/<int:post_id>/comentarios/', ComentariosList.as_view(), name='listar_criar_comentarios'),

    # Leitura, atualização e exclusão para um comentário
    path('comentarios/<int:comentario_id>/', ComentarioDetail.as_view(), name='detalhar_comentario'),

    # Curtir e descurtir um comentário
    path('comentarios/<int:comentario_id>/<str:action>/', ComentarioCurtir.as_view(), name='curtir_descurtir_comentario'),
]
