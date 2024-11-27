from django.urls import path
from .views import UsersAPIView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Listar e criar usuários (GET e POST)
    path('users/', UsersAPIView.as_view(), name='users-list-create'),

    # Atualizar e deletar um usuário específico (PUT e DELETE)
    path('users/<int:pk>/', UsersAPIView.as_view(), name='users-update-delete'),

    # Endpoints para obtenção e renovação do token JWT
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
