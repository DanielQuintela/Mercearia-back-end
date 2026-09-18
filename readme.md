# Mercearia API

API REST para gerenciamento de uma mercearia, com recursos para produtos, categorias, produtores, usuários e promoções.

A aplicação foi construída com Flask e segue uma organização em camadas, separando rotas, serviços, modelos, schemas e middlewares.

## Funcionalidades

- Autenticação de usuários com JWT.
- Cadastro e gerenciamento de usuários.
- Gerenciamento de produtos, categorias, produtores e promoções.
- Validação e serialização de dados com Marshmallow.
- Hash de senhas com bcrypt.
- Identificadores ULID para entidades do sistema.
- Registro de ações em trilha de auditoria.
- Health check com verificação da conexão com o banco de dados.
- Tratamento centralizado de erros HTTP, validação e banco de dados.
- Migrações versionadas com Flask-Migrate e Alembic.

## Stack

- **Linguagem:** Python
- **Framework web:** Flask
- **ORM:** Flask-SQLAlchemy e SQLAlchemy
- **Banco de dados:** MySQL
- **Driver do banco:** PyMySQL
- **Migrações:** Flask-Migrate e Alembic
- **Validação e serialização:** Marshmallow, Marshmallow-SQLAlchemy e Flask-Marshmallow
- **Autenticação:** Flask-JWT-Extended
- **Segurança de senhas:** bcrypt
- **Identificadores:** ULID
- **Configuração:** python-dotenv e variáveis de ambiente

## Arquitetura

```text
.
├── app.py                    # Ponto de entrada da aplicação
├── app/
│   ├── blueprints/           # Blueprints, incluindo autenticação
│   ├── common/               # Constantes e enums compartilhados
│   ├── middleware/           # Logs, validações e tratamento de erros
│   ├── models/               # Modelos persistidos no banco
│   ├── routes/               # Rotas dos recursos da API
│   ├── schemas/              # Schemas de entrada e saída
│   ├── services/             # Regras de negócio
│   └── utils/                # Utilitários, como criptografia de senhas
├── migrations/               # Configuração e versões das migrações
├── requirements.txt          # Dependências Python
└── readme.md
```

## Pré-requisitos

- Python 3.10 ou superior
- MySQL em execução
- `pip` atualizado

## Instalação

Clone o repositório e crie um ambiente virtual:

```bash
git clone <URL_DO_REPOSITORIO>
cd mercearia-back-end
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
FLASK_ENV=development
DATABASE_URL_DEV=mysql+pymysql://usuario:senha@localhost/mercearia
DATABASE_URL=mysql+pymysql://usuario:senha@localhost/mercearia
SECRET_KEY=altere-esta-chave
JWT_SECRET_KEY=altere-esta-chave-jwt
JWT_ACCESS_TOKEN_EXPIRES=3600
```

Em desenvolvimento, a aplicação usa `DATABASE_URL_DEV`. Em produção, usa `DATABASE_URL`.

## Banco de dados e migrações

Para aplicar as migrações existentes:

```bash
flask --app app.py db upgrade
```

Para criar uma nova migração após alterar os modelos:

```bash
flask --app app.py db migrate -m "descricao da migracao"
flask --app app.py db upgrade
```

## Execução

Com o ambiente virtual ativado e o banco configurado:

```bash
python app.py
```

A API ficará disponível por padrão em `http://127.0.0.1:5000`.

## Endpoints principais

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/api/v1/` | Verifica se a API está online |
| `GET` | `/api/v1/health` | Verifica a conexão com o banco |
| `POST` | `/api/v1/login` | Autentica um usuário e retorna um JWT |
| `...` | `/api/v1/products` | Operações de produtos |
| `...` | `/api/v1/categories` | Operações de categorias |
| `...` | `/api/v1/producers` | Operações de produtores |
| `...` | `/api/v1/users` | Operações de usuários |
| `...` | `/api/v1/promotions` | Operações de promoções |

Os endpoints protegidos devem receber o token JWT no cabeçalho:

```http
Authorization: Bearer <TOKEN>
```

## Licença

© 2025 Daniel Quintela. Todos os direitos reservados.

O uso, cópia, modificação ou redistribuição deste código depende de autorização expressa do autor.
