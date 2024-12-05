# transparencia-ja-backend
Backend da aplicação Transparência Já

# Estrutura do Projeto

1. **Users**: Gerenciamento de usuários (cidadãos, gestores e administradores).
2. **Posts**: Publicação de informações relevantes para o público.
3. **Notificações**: Envio de notificações para os usuários.
4. **Contratantes**: Gerenciamento de contratantes (empresas e organizações que contratam serviços públicos).
5. **Comentários**: Sistema de comentários para posts.

---

# Endpoints

### **1. Users - Usuários**

- **GET /api/users/**: Lista todos os usuários.
- **POST /api/users/**: Cria um novo usuário.
- **GET /api/users/{id}/**: Detalha um usuário específico.
- **PUT /api/users/{id}/**: Atualiza os dados de um usuário.
- **DELETE /api/users/{id}/**: Deleta um usuário.

    #### **Exemplo de JSON para os Endpoints**

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

### **2. Posts - Publicações**

- **GET /api/posts/**: Lista todos os posts. É possível filtrar por `tipo` e `status`.
- **POST /api/posts/**: Cria um novo post.
- **GET /api/posts/{id}/**: Detalha um post específico.
- **PUT /api/posts/{id}/**: Atualiza um post.
- **DELETE /api/posts/{id}/**: Deleta um post.

    #### **Exemplo de JSON para os Endpoints**

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

### **3. Notificações**

- **GET /api/notificacoes/**: Lista todas as notificações.
- **POST /api/notificacoes/**: Cria uma nova notificação e envia para usuários específicos ou todos os usuários.
- **GET /api/notificacoes/{id}/**: Detalha uma notificação específica.
- **PUT /api/notificacoes/{id}/**: Atualiza uma notificação.
- **DELETE /api/notificacoes/{id}/**: Deleta uma notificação.

    #### **Exemplo de JSON para os Endpoints**

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

### **4. Contratantes**

- **GET /api/contratantes/**: Lista todos os contratantes.
- **POST /api/contratantes/**: Cria um novo contratante.
- **GET /api/contratantes/{id}/**: Detalha um contratante específico.
- **PUT /api/contratantes/{id}/**: Atualiza um contratante específico.
- **DELETE /api/contratantes/{id}/**: Deleta um contratante específico.

    #### Exemplo de JSON para os Endpoints

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

### **5. Comentários**

- **GET /api/posts/{post_id}/comentarios/**: Lista todos os comentários de um post específico.
- **POST /api/posts/{post_id}/comentarios/criar/**: Cria um novo comentário em um post específico.
- **GET /api/comentarios/{comentario_id}/**: Detalha um comentário específico.
- **POST /api/comentarios/{comentario_id}/curtir/**: Incrementa o número de likes de um comentário.
- **POST /api/comentarios/{comentario_id}/descurtir/**: Incrementa o número de deslikes de um comentário.

    #### **Exemplo de JSON para os Endpoints**

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
