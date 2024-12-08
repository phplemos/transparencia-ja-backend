from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Definindo a visualização do schema
schema_view = get_schema_view(
   openapi.Info(
      title="Transparência Já - API",
      default_version='v1',
      description=""" 
        A API **Transparência Já** é um sistema desenvolvido para fornecer informações transparentes e acessíveis sobre obras e projetos públicos em andamento. 
        Ela permite a consulta de dados, envio de notificações sobre mudanças e interação direta com os cidadãos. 

        A API oferece funcionalidades abrangentes que facilitam o gerenciamento de usuários, posts, contratantes, comentários e notificações, com o objetivo de manter a população informada e engajada nas ações e projetos da sua comunidade.

        ### Principais recursos da API:
        - **Gestão de usuários**: Cadastro e gerenciamento de usuários com diferentes papéis (gestor, cidadão).
        - **Postagens**: Criação, listagem e edição de posts relacionados a obras, projetos e atualizações na cidade.
        - **Contratantes**: Gerenciamento de informações sobre contratantes de obras e projetos.
        - **Comentários**: Possibilidade de interação entre os cidadãos com posts e projetos, permitindo feedbacks.
        - **Notificações**: Envio de notificações sobre atualizações importantes para cidadãos e gestores.

        Os verbos HTTP foram organizados para facilitar a navegação e manipulação dos dados de cada tabela do modelo, proporcionando acesso direto e claro às informações públicas e interações disponíveis. Cada recurso foi implementado com clareza e simplicidade, permitindo que os usuários consultem, criem e atualizem informações de forma eficaz.

        Esta documentação apresenta todas as rotas disponíveis e seus respectivos verbos HTTP, facilitando a integração e uso da API.
        """,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="fernando.ibirataia0@gmail.com"),
      license=openapi.License(name="Licença da API Transparência Já"),
   ),
   public=True,  # Tornar a documentação pública
   permission_classes=(permissions.AllowAny,),  # Permitir acesso sem autenticação
   authentication_classes=[],  # Desabilitar autenticação para acesso ao Swagger
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls' )),
    path('api/', include('posts.urls' )),
    path('api/', include('contratantes.urls')),
    path('api/', include('comentarios.urls')),
    path('api/', include('notificacoes.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),  # Rota para acessar a documentação
]
