# transparencia-ja-backend
Backend da aplicação Transparência Já

## Transparência Já - Sistema de Gestão Social Integrada

### **Sobre a API**

Esta API foi desenvolvida como resultado final de um hackathon promovido pela Cepedi, no projeto **Restic36**, realizado no polo de Jequié-BA. Este é o **MVP** de um sistema inovador para gestão social integrada, que visa aumentar a **participação cidadã** e a **transparência governamental**.

---

### **Motivação e Problema Identificado**

A proposta "Transparência Já" surge para enfrentar a crônica falta de transparência nas decisões públicas e a baixa participação cidadã, mesmo com legislações como:

- **Lei de Acesso à Informação (LAI)**: exige a divulgação de dados públicos, mas falha em garantir clareza e acessibilidade.
- **Portais de Transparência**: frequentemente desorganizados, com linguagem técnica complexa, dificultam o acompanhamento pelos cidadãos.
- **Acesso via Dispositivos Móveis**: a maioria dos brasileiros utiliza smartphones como principal meio de acesso à internet (segundo o IBGE), mas muitos portais não são otimizados para esses dispositivos.

Essas barreiras comprometem a confiança da sociedade nas instituições públicas, dificultando o controle social.

---

### **A Solução: Transparência Já**

O **Transparência Já** propõe um **aplicativo móvel** intuitivo e acessível, que democratiza o acesso às informações públicas e promove a interação entre governos e cidadãos.

### **Principais Funcionalidades**
1. **Notificações Personalizadas**
   - Atualizações em tempo real sobre obras públicas, decisões governamentais, contratos e status de solicitações.
   - Foco nas áreas de interesse do cidadão.

2. **Canal de Comunicação Direta**
   - Feedback ativo entre prefeituras e cidadãos, facilitando sugestões, reclamações e dúvidas.
   - Suporte a emergências, como desastres naturais, por meio de **alertas geolocalizados**.

3. **Gamificação**
   - Simulações práticas para que cidadãos compreendam a gestão pública (ex.: alocação de recursos orçamentários).
   - Reconhecimentos virtuais para incentivar a participação contínua.

4. **Mapa Interativo**
   - Visualização de obras e projetos com informações detalhadas (prazos, orçamentos, impactos).
   - Registro de sugestões e preocupações diretamente vinculadas aos projetos no mapa.

5. **Apoio à Participação Cidadã**
   - Consultas públicas, fóruns e enquetes interativas para engajar a população nas decisões governamentais.

---

### **Estrutura do Projeto**

1. **Users**: Gerenciamento de usuários (cidadãos, gestores e administradores).
2. **Posts**: Publicação de informações relevantes para o público.
3. **Notificações**: Envio de notificações para os usuários.
4. **Contratantes**: Gerenciamento de contratantes (empresas e organizações que contratam serviços públicos).
5. **Comentários**: Sistema de comentários para posts.

---

### **Endpoints**

#### **1. Users - Usuários**

- **GET /api/users/**: Lista todos os usuários.
- **POST /api/users/**: Cria um novo usuário.
- **GET /api/users/{id}/**: Detalha um usuário específico.
- **PUT /api/users/{id}/**: Atualiza os dados de um usuário.
- **DELETE /api/users/{id}/**: Deleta um usuário.
- **POST /api/login/**  
* Gera um token de autenticação (JWT) para o usuário.  
  **Parâmetros no corpo da requisição**:  
  ```json
    {
        "username": "seu_username",
        "password": "sua_senha"
    }

##### **Exemplo de JSON para os Endpoints**

- **GET /api/users/**: Lista todos os usuários.

    **Exemplo de Resposta (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "nome": "João Silva",
            "email": "joao.silva@example.com",
            "papel": "admin",
            "pontos": 0.0,
            "nivel": 1
        }
    ]

#### **2. Posts - Publicações**

- **GET /api/posts/**: Lista todos os posts. É possível filtrar por `tipo` e `status`.
- **POST /api/posts/**: Cria um novo post.
- **GET /api/posts/{id}/**: Detalha um post específico.
- **PUT /api/posts/{id}/**: Atualiza um post.
- **DELETE /api/posts/{id}/**: Deleta um post.

    ##### **Exemplo de JSON para os Endpoints**

    - **GET /api/posts/**: Lista todos os posts.

    **Exemplo de Resposta (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "titulo": "Promoção de Verão",
            "descricao": "Descontos incríveis em artigos esportivos.",
            "localizacao": "São Paulo",
            "imagem": "link_para_imagem.jpg",
            "tipo": "Promoção",
            "status": "Ativo",
            "pdf": null,
            "likes": 0,
            "deslikes": 0,
            "comentarios": [
                {
                    "id": 1,
                    "texto": "Ótimos descontos! Vou aproveitar!",
                    "post": 1,
                    "post_titulo": "Promoção de Verão",
                    "user": 1,
                    "user_nome": "João Silva",
                    "data_criacao": "2024-12-05T05:16:32.766506Z",
                    "likes": 0,
                    "deslikes": 0
                },
                {
                    "id": 2,
                    "texto": "Não vou nessa loja!! Eca!!",
                    "post": 1,
                    "post_titulo": "Promoção de Verão",
                    "user": 1,
                    "user_nome": "João Silva",
                    "data_criacao": "2024-12-05T05:17:39.819474Z",
                    "likes": 0,
                    "deslikes": 0
                }
            ],
            "user_id": 1,
            "contratantes": [1, 2]
        }
    ]

#### **3. Notificações**

- **GET /api/notificacoes/**: Lista todas as notificações.
- **POST /api/notificacoes/**: Cria uma nova notificação e envia para usuários específicos ou todos os usuários.
- **GET /api/notificacoes/{id}/**: Detalha uma notificação específica.
- **PUT /api/notificacoes/{id}/**: Atualiza uma notificação.
- **DELETE /api/notificacoes/{id}/**: Deleta uma notificação.

    ##### **Exemplo de JSON para os Endpoints**

    - **GET /api/notificacoes/**: Lista todas as notificações.

    **Exemplo de Resposta (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "titulo": "Novas atualizações de serviço",
            "mensagem": "O sistema foi atualizado com novas funcionalidades.",
            "data_envio": "2024-12-05T09:00:00",
            "usuarios_alvo": [1, 2, 3],
            "status": "Enviada"
        },
        {
            "id": 2,
            "titulo": "Promoção de Natal",
            "mensagem": "Descontos especiais em diversos produtos!",
            "data_envio": "2024-12-05T10:00:00",
            "usuarios_alvo": [2, 4],
            "status": "Pendente"
        }
    ]

#### **4. Contratantes**

- **GET /api/contratantes/**: Lista todos os contratantes.
- **POST /api/contratantes/**: Cria um novo contratante.
- **GET /api/contratantes/{id}/**: Detalha um contratante específico.
- **PUT /api/contratantes/{id}/**: Atualiza um contratante específico.
- **DELETE /api/contratantes/{id}/**: Deleta um contratante específico.

    ##### **Exemplo de JSON para os Endpoints**

    - **GET /api/contratantes/**: Lista todos os contratantes.

    **Exemplo de Resposta (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "nome": "Calçados SuperFit",
            "cnpj": "12.345.678/0001-90",
            "email": "contato@superfitcalçados.com.br"
        },
        {
            "id": 2,
            "nome": "SportMax",
            "cnpj": "98.765.432/0001-12",
            "email": "contato@sportmax.com.br"
        }
    ]

#### **5. Comentários**

- **GET /api/posts/{post_id}/comentarios/**: Lista todos os comentários de um post específico.
- **POST /api/posts/{post_id}/comentarios/criar/**: Cria um novo comentário em um post específico.
- **GET /api/comentarios/{comentario_id}/**: Detalha um comentário específico.
- **POST /api/comentarios/{comentario_id}/curtir/**: Incrementa o número de likes de um comentário.
- **POST /api/comentarios/{comentario_id}/descurtir/**: Incrementa o número de deslikes de um comentário.

    ##### **Exemplo de JSON para os Endpoints**

    - **GET /api/posts/{post_id}/comentarios/**: Lista todos os comentários de um post específico.

    **Exemplo de Resposta (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "texto": "Ótimos descontos! Vou aproveitar!",
            "post": 1,
            "post_titulo": "Promoção de Verão",
            "user": 1,
            "user_nome": "João Silva",
            "data_criacao": "2024-12-05T05:16:32.766506Z",
            "likes": 0,
            "deslikes": 0
        },
        {
            "id": 2,
            "texto": "Não vou nessa loja!! Eca!!",
            "post": 1,
            "post_titulo": "Promoção de Verão",
            "user": 1,
            "user_nome": "João Silva",
            "data_criacao": "2024-12-05T05:17:39.819474Z",
            "likes": 0,
            "deslikes": 0
        }
    ]

---

### **Testes Automatizados**

#### **1. Testes de Usuários (UserTests)**
- **`test_criar_usuario`**: Verifica a criação de um novo usuário autenticado.
- **`test_criar_usuario_com_geolocalizacao`**: Testa a criação de um usuário com dados de geolocalização (bairro e rua).
- **`test_usuario_nao_autenticado`**: Garante que um usuário não autenticado não pode criar um perfil.
- **`test_permissao_acesso_gerenciamento`**: Valida se um usuário autenticado pode editar seu próprio perfil.
- **`test_usuarios_nao_autenticados_nao_podem_criar_ou_editar`**: Garante que usuários não autenticados não podem criar ou editar perfis.
- **`test_listagem_de_usuarios_para_usuario_autenticado`**: Verifica se usuários autenticados podem listar perfis.
- **`test_listagem_de_usuarios_para_usuario_nao_autenticado`**: Testa a restrição de listagem de usuários para não autenticados.

#### **2. Testes de Posts (PostTests)**
- **`test_listar_posts`**: Garante que posts podem ser listados por usuários autenticados.
- **`test_criar_post`**: Valida a criação de novos posts.
- **`test_get_post`**: Verifica a consulta de posts específicos.
- **`test_atualizar_post`**: Testa a atualização de posts existentes.
- **`test_deletar_post`**: Verifica a exclusão de posts.
- **`test_usuarios_nao_autenticados_nao_podem_criar_ou_editar`**: Garante que usuários não autenticados não podem criar ou editar posts.

#### **3. Testes de Notificações (NotificacaoTests)**
- **`test_criar_notificacao`**: Testa a criação de novas notificações.
- **`test_listar_notificacoes`**: Valida a listagem de notificações existentes.
- **`test_atualizar_notificacao`**: Garante a atualização correta de notificações.

#### **4. Testes de Contratantes (ContratanteTests)**
- **`test_criar_contratante`**: Verifica a criação de contratantes.
- **`test_listar_contratantes`**: Valida a listagem de contratantes.
- **`test_atualizar_contratante`**: Testa a atualização de dados de contratantes.
- **`test_deletar_contratante`**: Garante a exclusão de contratantes.
- **`test_obter_contratante_inexistente`**: Testa o acesso a contratantes inexistentes.
- **`test_atualizar_contratante_inexistente`**: Verifica a tentativa de atualizar contratantes inexistentes.
- **`test_deletar_contratante_inexistente`**: Testa a exclusão de contratantes inexistentes.

#### **5. Testes de Comentários (ComentarioTests)**
- **`test_deletar_comentario_com_papel_gestor`**: Verifica se gestores podem excluir comentários.
- **`test_listar_comentarios`**: Valida a listagem de comentários de posts.
- **`test_atualizar_comentario`**: Testa a atualização de comentários existentes.
- **`test_deletar_comentario_inexistente`**: Garante o tratamento correto ao tentar excluir comentários inexistentes.

---

### **Passos para Execução dos Testes**

1. Certifique-se de que todas as dependências estão instaladas:
   - Django, DRF, JWT e demais bibliotecas especificadas no projeto.
2. Verifique a configuração do banco de dados de testes.
   - O Django cria automaticamente um banco de dados temporário para os testes, que é descartado após sua execução.
3. Execute os testes com o seguinte comando:
   ```bash
   python manage.py test

---

### **Benefícios do Sistema**

#### **Para os Gestores Públicos**
- Melhoria na comunicação com a população.
- Identificação precisa das demandas prioritárias.
- Administração transparente e eficiente, fortalecendo a confiança institucional.

#### **Para os Cidadãos**
- Acesso claro e prático às informações públicas.
- Ferramentas para fiscalizar ações governamentais.
- Participação ativa em decisões e políticas públicas.

#### **Para Outros Setores**
- Jornalistas: acesso simplificado a dados para investigações.
- ONGs e Associações: colaboração eficiente com dados organizados.

---

### **Sustentabilidade do Projeto**

O **Transparência Já** é uma solução escalável e sustentável, que se alinha às tendências globais de governo aberto. Sua relevância será mantida por meio de:

- Atualizações tecnológicas constantes.
- Personalização de funcionalidades para atender às demandas locais.
- Integração de novos dados públicos e ferramentas de engajamento.

---

### **Acesso à Documentação Interativa**

A documentação pode ser acessada diretamente no navegador através da seguinte rota:
   ```bash
   http://127.0.0.1:8000/swagger/
