from django.urls import path
from . import views

urlpatterns = [
    path('contratantes/', views.listar_contratantes, name='listar_contratantes'),  # Endpoint para listar contratantes
    path('criar/', views.criar_contratante, name='criar_contratante'),  # Endpoint para criar um contratante
    path('<int:id>/', views.visualizar_contratante, name='visualizar_contratante'),  # Endpoint para visualizar um contratante específico
]
