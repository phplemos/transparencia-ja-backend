from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:post_id>/comentarios/', views.listar_comentarios, name='listar_comentarios'),
    path('posts/<int:post_id>/comentarios/criar/', views.criar_comentario, name='criar_comentario'),
    path('comentarios/<int:comentario_id>/', views.visualizar_comentario, name='visualizar_comentario'),
    path('comentarios/<int:comentario_id>/curtir/', views.curtir_comentario, name='curtir_comentario'),
    path('comentarios/<int:comentario_id>/descurtir/', views.descurtir_comentario, name='descurtir_comentario'),
]
