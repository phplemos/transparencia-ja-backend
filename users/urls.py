from django.urls import path
from .views import UsersAPIView

urlpatterns = [
     # Listar e criar usuários (GET e POST)
    path('users/', UsersAPIView.as_view(), name='users-list-create'),
    
    # Atualizar e deletar um usuário específico (PUT e DELETE)
    path('users/<int:pk>/', UsersAPIView.as_view(), name='users-update-delete'),
]
