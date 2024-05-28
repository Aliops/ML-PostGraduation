# ML- entrega.

## Descrição

Este projeto é uma API desenvolvida com FastAPI que realiza operações de autenticação, manipulação de dados e scraping de dados de produção, processamento, comercialização, importação e exportação de produtos.

## Estrutura do Projeto

- **auth.py**: Contém funções para criação e decodificação de tokens JWT.
- **database.py**: Configuração do banco de dados SQLite.
- **datacess.py**: Funções para web scraping de dados de produção, processamento, comercialização, importação e exportação.
- **entities.py**: Modelos de dados Pydantic e SQLAlchemy.
- **models.py**: Modelos de dados Pydantic para usuários e tokens.
- **utils.py**: Funções utilitárias para hash e verificação de senhas.
- **main.py**: Configuração principal do FastAPI e endpoints da API.

## Requisitos

- Python 3.9+
- FastAPI
- SQLAlchemy
- Pydantic
- Pandas
- Passlib
- python-jose

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seu-repositorio
    ```

3. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1. Configure a chave secreta para JWT em `auth.py`:

    ```python
    SECRET_KEY = "sua-chave-secreta"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    ```

2. Configure o URL do banco de dados em `database.py`:

    ```python
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    ```

## Execução

1. Inicie a aplicação FastAPI:

    ```bash
    uvicorn main:app --reload
    ```

2. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints

### Autenticação

- **POST /token**: Gera um token de acesso para autenticação.
  - Request: `username` e `password`
  - Response: `access_token` e `token_type`

### Usuários

- **POST /users/**: Cria um novo usuário.
  - Request: `username`, `email`, `password`
  - Response: Detalhes do usuário criado

- **GET /users/me**: Retorna detalhes do usuário autenticado.
  - Response: Detalhes do usuário

### Dados de Produção

- **GET /producao/{year}**: Retorna dados de produção para o ano especificado.
  - Request: `year`
  - Response: Lista de produções

### Dados de Processamento

- **GET /processamento/{year}/{subopt}**: Retorna dados de processamento para o ano e subopção especificados.
  - Request: `year`, `subopt`
  - Response: Lista de processamentos

### Dados de Comercialização

- **GET /comercializacao/{year}**: Retorna dados de comercialização para o ano especificado.
  - Request: `year`
  - Response: Lista de comercializações

### Dados de Importação

- **GET /importacao/{year}/{subopt}**: Retorna dados de importação para o ano e subopção especificados.
  - Request: `year`, `subopt`
  - Response: Lista de importações

### Dados de Exportação

- **GET /exportacao/{year}/{subopt}**: Retorna dados de exportação para o ano e subopção especificados.
  - Request: `year`, `subopt`
  - Response: Lista de exportações


### Autenticação

1. Obtenha um token de acesso:

    ```bash
    curl -X POST "http://127.0.0.1:8000/token" -d "username=seu-usuario&password=sua-senha"
    ```

2. Utilize o token para acessar os endpoints protegidos:

    ```bash
    curl -H "Authorization: Bearer seu-token" "http://127.0.0.1:8000/users/me"
    ```

### Acessando Dados de Produção

1. Acesse os dados de produção para um determinado ano:

    ```bash
    curl "http://127.0.0.1:8000/producao/2023"
    ```

## Contribuição

1. Fork este repositório
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
