# Flix API

## Descrição

**Flix API** é uma API desenvolvida para simular um serviço de streaming de filmes. Utilizando SQLite3 como banco de dados e Django Rest Framework (DRF) para criar a API, o projeto permite gerenciar filmes, categorias e atores de uma maneira eficiente e escalável.

## Tecnologias

- **Django**: Framework web em Python para desenvolver a API.
- **Django Rest Framework (DRF)**: Biblioteca para construir APIs RESTful com Django.
- **Docker** (opcional): Para contêinerização do projeto.

## Funcionalidades

- **Gerenciamento de Filmes**: CRUD (Criar, Ler, Atualizar, Deletar) de filmes com detalhes como título, descrição, ano de lançamento, e gênero.
- **Gerenciamento de Categorias**: CRUD de categorias para classificar filmes.
- **Gerenciamento de Atores**: CRUD de atores para compor os filmes
- **Autenticação de Acesso**: Autenticação de quem acessa os dados da API através de uma chave disponibilizada
- **Busca e Filtros**: Pesquisa de filmes por título e filtros por categorias e ano de lançamento.

## Requisitos

- Python 3.8 ou superior
- pip (para instalar dependências Python)
- (Opcional) Docker

## Instalação

### 1. Clone o Repositório

Abra o terminal no VSCode e execute o seguinte comando para clonar o repositório:

git clone https://github.com/LuizH0412/flix-api.git

cd flix-api

## Endpoints

A API está organizada em vários módulos, cada um com seus próprios endpoints. Abaixo estão os detalhes dos principais endpoints disponíveis:

### Authentication

- **/api/v1/auth/**: (Endpoints para autenticação e gestão de usuários. Detalhes específicos dos endpoints devem ser verificados no módulo `authentication.urls`.)

### Generos

- **/api/v1/generos/**: (Endpoints para gerenciamento de gêneros de filmes. Detalhes específicos dos endpoints devem ser verificados no módulo `generos.urls`.)

### Atores

- **/api/v1/atores/**: (Endpoints para gerenciamento de atores. Detalhes específicos dos endpoints devem ser verificados no módulo `atores.urls`.)

### Filmes

- **/api/v1/filmes/**: (Endpoints para gerenciamento de filmes. Detalhes específicos dos endpoints devem ser verificados no módulo `filmes.urls`.)

### Reviews

- **/api/v1/reviews/**: (Endpoints para gerenciamento de avaliações de filmes. Detalhes específicos dos endpoints devem ser verificados no módulo `reviews.urls`.)

