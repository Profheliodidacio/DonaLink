# API Documentation - DonaLink

Bem-vindo à documentação da API do DonaLink, uma aplicação de doações para causas sociais. Esta API permite acessar e interagir com os dados e funcionalidades do aplicativo, como autenticação de usuários, consulta de informações sobre causas e gerenciamento de doações.

---

## Índice

- [Autenticação](#autenticação)
  - [Login de Usuário](#login-de-usuário)
- [Causas e Doações](#causas-e-doações)
  - [Listar Causas Disponíveis](#listar-causas-disponíveis)
  - [Realizar Doação](#realizar-doação)
- [Informações do Usuário](#informações-do-usuário)
  - [Obter Detalhes do Usuário](#obter-detalhes-do-usuário)

---

## Autenticação

### Login de Usuário

- **Rota**: `/api/auth/login`
- **Método**: `POST`
- **Descrição**: Autentica o usuário e retorna um token de acesso.
- **Parâmetros**:
  - `email` (string): Email do usuário.
  - `password` (string): Senha do usuário.
- **Resposta de Sucesso**:
  ```json
  {
    "status": "success",
    "message": "Usuário autenticado com sucesso",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
