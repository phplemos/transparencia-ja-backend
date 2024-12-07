from django.urls import path
from .views import NotificacaoList, NotificacaoDetail

urlpatterns = [
    path("notificacoes/", NotificacaoList.as_view(), name="notificacao_list"),  # Listar/criar notificações
    path("notificacoes/<int:pk>/", NotificacaoDetail.as_view(), name="notificacao_detail"),  # Detalhar/atualizar/excluir notificação
]
