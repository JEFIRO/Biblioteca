# Biblioteca Online

Este projeto é uma aplicação web para a gestão de uma biblioteca online. Ele permite o cadastro de livros, clientes e a gestão de empréstimos de livros.

## Funcionalidades

- **Cadastro de Livros**: Permite cadastrar novos livros na biblioteca.
- **Busca de Livros**: Permite buscar livros pelo nome.
- **Cadastro de Clientes**: Permite cadastrar novos clientes.
- **Gestão de Empréstimos**: Permite registrar empréstimos de livros a clientes e listar todos os empréstimos.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Java com Spring Boot
- **Banco de Dados**: H2 Database (pode ser configurado para outro banco de dados)
## API

A aplicação também fornece uma API RESTful para interação com os recursos de livros, clientes e empréstimos.

### Endpoints Principais

- **Livros**
  - `GET /api/livros`: Lista todos os livros.
  - `POST /api/livros`: Cria um novo livro.
  - `GET /api/livros/{id}`: Obtém os detalhes de um livro específico.
  - `GET /api/livros/buscar`: Busca livros pelo nome.

- **Clientes**
  - `GET /api/clientes`: Lista todos os clientes.
  - `POST /api/clientes`: Cria um novo cliente.

- **Empréstimos**
  - `GET /api/emprestimos`: Lista todos os empréstimos.
  - `POST /api/emprestimos`: Cria um novo empréstimo.
  - 
- **Projeto em desenvolvimento**
  
