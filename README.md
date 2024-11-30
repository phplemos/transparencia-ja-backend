# transparencia-ja-backend
Backend da aplicação Transparencia ja

## Estrutura do Projeto

1. **Users**: Gerenciamento de usuários (cidadãos e administradores).
2. **Posts**: Publicação de informações relevantes para o público.
3. **Notificações**: Envio de notificações para os usuários.
4. **Contratantes**: Gerenciamento de contratantes (empresas e organizações que contratam serviços públicos).
5. **Comentários**: Sistema de comentários para posts.

## Endpoints

### **1. Users - Usuários**

- **GET /api/users/**: Lista todos os usuários.
- **POST /api/users/**: Cria um novo usuário.
- **GET /api/users/{id}/**: Detalha um usuário específico.
- **PUT /api/users/{id}/**: Atualiza os dados de um usuário.
- **DELETE /api/users/{id}/**: Deleta um usuário.

### **2. Posts - Publicações**

- **GET /api/posts/**: Lista todos os posts. É possível filtrar por `tipo` e `status`.
- **POST /api/posts/**: Cria um novo post.
- **GET /api/posts/{id}/**: Detalha um post específico.
- **PUT /api/posts/{id}/**: Atualiza um post.
- **DELETE /api/posts/{id}/**: Deleta um post.

### **3. Notificações**

- **GET /api/notificacoes/**: Lista todas as notificações.
- **POST /api/notificacoes/**: Cria uma nova notificação e envia para usuários específicos ou todos os usuários.
- **GET /api/notificacoes/{id}/**: Detalha uma notificação específica.
- **PUT /api/notificacoes/{id}/**: Atualiza uma notificação.
- **DELETE /api/notificacoes/{id}/**: Deleta uma notificação.

### **4. Contratantes**

- **GET /api/contratantes/**: Lista todos os contratantes.
- **POST /api/contratantes/**: Cria um novo contratante.
- **GET /api/contratantes/{id}/**: Detalha um contratante específico.

### **5. Comentários**

- **GET /api/posts/{post_id}/comentarios/**: Lista todos os comentários de um post específico.
- **POST /api/posts/{post_id}/comentarios/criar/**: Cria um novo comentário em um post específico.
- **GET /api/comentarios/{comentario_id}/**: Detalha um comentário específico.
- **POST /api/comentarios/{comentario_id}/curtir/**: Incrementa o número de likes de um comentário.
- **POST /api/comentarios/{comentario_id}/descurtir/**: Incrementa o número de deslikes de um comentário.


