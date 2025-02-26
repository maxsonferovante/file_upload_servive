**Clean Architecture** com **FastAPI**:

---

## Estrutura de Pastas

```
project-root/
│
├── app/
│   ├── main.py               # Ponto de entrada da aplicação FastAPI
│   │
│   ├── api/
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── upload_router.py  # Definição dos endpoints de upload
│   │   │   ├── status_router.py  # Definição dos endpoints de status
│   │   │   └── schemas.py        # Definição dos modelos de request/response
│   │   │
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py             # Configurações da aplicação (ex: variáveis de ambiente)
│   │   └── exceptions.py         # Definição de exceções customizadas
│   │
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── file_model.py     # Definição das entidades do domínio (ex: File)
│   │   │
│   │   └── repositories/
│   │       ├── __init__.py
│   │       └── file_repository.py  # Interface para repositórios (ex: consulta de status)
│   │
│   ├── usecases/
│   │   ├── __init__.py
│   │   ├── upload_file.py        # Caso de uso para upload
│   │   ├── confirm_upload.py     # Caso de uso para confirmar upload
│   │   └── update_status.py      # Caso de uso para atualizar status
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── s3_service.py         # Serviço para operações no S3
│   │   └── sqs_service.py        # Serviço para envio de mensagens para o SQS
│   │
│   └── infrastructure/
│       ├── __init__.py
│       ├── database.py           # Conexão com banco de dados (se necessário)
│       └── file_repository_impl.py # Implementação do repositório de status
│
├── tests/
│   ├── __init__.py
│   ├── test_upload.py            # Testes para o endpoint de upload
│   ├── test_confirm_upload.py    # Testes para o endpoint de confirmação
│   └── test_update_status.py     # Testes para o endpoint de atualização de status
│
├── Dockerfile                    # Dockerfile para containerizar a aplicação
├── docker-compose.yml             # Configuração do Docker Compose (opcional)
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação do projeto
```

---

## Descrição da Estrutura

1. **app/main.py**: Ponto de entrada do FastAPI, responsável por iniciar o servidor e registrar os roteadores.

2. **api/v1**:

   - `upload_router.py`: Definição dos endpoints para upload.
   - `status_router.py`: Definição dos endpoints para confirmação e atualização de status.
   - `schemas.py`: Modelos de request e response para validação e documentação.

3. **core**:

   - `config.py`: Configurações gerais da aplicação, como variáveis de ambiente.
   - `exceptions.py`: Exceções customizadas para controle de erros.

4. **domain**:

   - `models`: Entidades do domínio (ex: `File`) que representam as regras de negócio.
   - `repositories`: Interfaces para acessar o banco de dados ou qualquer outra fonte de dados.

5. **usecases**:

   - Define os casos de uso (regras de negócio) da aplicação, como:
     - `upload_file.py`: Gera a URL pré-assinada e o ID único.
     - `confirm_upload.py`: Confirma o upload e envia mensagem ao SQS.
     - `update_status.py`: Atualiza o status do processamento.

6. **services**:

   - Serviços externos e integrações, como:
     - `s3_service.py`: Operações com o S3 (ex: gerar URL pré-assinada).
     - `sqs_service.py`: Envio de mensagens para o SQS.

7. **infrastructure**:

   - Implementações das interfaces definidas em `domain/repositories`.
   - `database.py`: Configuração de banco de dados (caso necessário).
   - `file_repository_impl.py`: Implementação para consulta de status de upload.

8. **tests**:
   - Testes automatizados para garantir a qualidade e estabilidade do sistema.

---

## Benefícios da Clean Architecture

- **Independência de frameworks:** Fácil de trocar o FastAPI por outro framework.
- **Testabilidade:** Casos de uso são facilmente testáveis de forma isolada.
- **Independência de banco de dados e serviços externos:** Facilita a troca de infraestrutura (S3, SQS, etc.).
- **Manutenção e Evolução:** Estrutura modular e desacoplada.
