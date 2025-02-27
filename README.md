# File Upload Service

Este serviço de upload de arquivos oferece uma maneira eficiente de armazenar arquivos no Amazon S3 utilizando URLs pré-assinadas, monitorar o status do upload e gerenciar o processamento dos arquivos com mensagens SQS e uma função Lambda.

## Visão Geral

O sistema é composto por três endpoints principais:

1. **Upload de Arquivo:** Gera uma URL pré-assinada para upload direto no S3 e retorna um ID único para acompanhar o status do upload.
2. **Confirmação de Upload:** Recebe a confirmação de que o arquivo foi salvo no S3 e aciona uma mensagem no SQS para processar o arquivo.
3. **Atualização de Status:** Atualiza o status do processamento do arquivo, conforme a execução da função Lambda.

---

## Endpoints

### 1. POST `/upload`

Recebe as informações do arquivo e retorna uma URL pré-assinada para upload no S3, além de um ID único para consulta do status do upload.

#### Parâmetros:

- `file_name`: Nome do arquivo.
- `extension`: Extensão do arquivo (ex: `.jpg`, `.pdf`).
- `len`: Tamanho do arquivo em bytes.
- `type`: Natureza do arquivo..

#### Retorno:

- `fields`: URL pré-assinada para upload direto no S3.
- `file_id`: ID único para acompanhar o status do upload.
- `file_name`

---

### 2. POST `/confirm-upload`

Confirma que o arquivo foi salvo no S3 e envia uma mensagem para o SQS para iniciar o processamento do arquivo.

#### Parâmetros:

- `file_id`: ID único do arquivo (gerado no endpoint `/upload`).

#### Processo:

- Ao receber a confirmação, o sistema envia uma mensagem para o SQS contendo:

  - `key_path`: Caminho do arquivo no S3.
  - `file_id`: ID único do arquivo.
  - `dest_path`: Caminho de destino no S3 após o processamento.

- A mensagem no SQS aciona uma função Lambda que:
  - Move o arquivo da pasta de temporários (`/temp`) para a pasta de destino (`/dest`).
  - Atualiza o status do processamento via endpoint `/update-status`.

---

### 3. POST `/update-status`

Atualiza o status do processamento do arquivo na aplicação, conforme o progresso da função Lambda.

#### Parâmetros:

- `file_id`: ID único do arquivo.
- `status`: Novo status do processamento (ex: `processing`, `completed`, `error`).
- `details` (opcional): Detalhes adicionais sobre o status do processamento.

---

### 4. GET `/consult-status`

Fornece o status do processamento do arquivo na aplicação, conforme o progresso da função Lambda.

#### Parâmetros:

- `file_id`: ID único do arquivo.

Resposta

- `status`: Novo status do processamento (ex: `processing`, `completed`, `error`).
- `details` (opcional): Detalhes adicionais sobre o status do processamento.

---

## Fluxo de Processamento

1. **Upload de Arquivo:**

   - Cliente chama o endpoint `/upload` com as informações do arquivo.
   - API gera uma URL pré-assinada e retorna ao cliente junto com o `file_id`.
   - Cliente faz o upload do arquivo diretamente para o S3 usando a URL recebida.

2. **Confirmação de Upload:**

   - Cliente confirma o upload chamando o endpoint `/confirm-upload` com o `file_id`.
   - API envia uma mensagem para o SQS para iniciar o processamento.

3. **Processamento na Lambda:**

   - Função Lambda é acionada pela mensagem no SQS.
   - A Lambda move o arquivo da pasta temporária (`/temp`) para a pasta de destino (`/dest`) no S3.
   - Lambda atualiza o status do processamento chamando o endpoint `/update-status`.

4. **Atualização de Status:**
   - Cliente pode consultar o status do processamento através do `file_id`.
   - O status é atualizado pela Lambda conforme o processamento avança.

---

## Tecnologias Utilizadas

- **AWS S3:** Armazenamento de arquivos.
- **AWS SQS:** Fila de mensagens para acionar o processamento na Lambda.
- **AWS Lambda:** Processamento assíncrono para mover o arquivo.
- **PostgreSQL:** Para armazenar as informações do processo.
- **FastAPI:** Para construção da API.
- **Docker:** Para empacotamento e deploy da aplicação.
- **GitHub Actions:** CI/CD para construir e atualizar automaticamente a Lambda.

---

## Requisitos

- Python 3.x
- Boto3 (SDK AWS para Python)
- Docker (opcional para deploy)
- AWS CLI configurado com permissões para S3, SQS e Lambda

---

## Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/file-upload-service.git
cd file-upload-service

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente para AWS
export AWS_ACCESS_KEY_ID=seu_access_key
export AWS_SECRET_ACCESS_KEY=sua_secret_key
export AWS_REGION=sua_regiao

# Execute a aplicação
python app.py
```

---

## Configuração no AWS

1. **S3:** Crie um bucket com as pastas `temp/` e `dest/`.
2. **SQS:** Configure uma fila para acionar a Lambda.
3. **Lambda:** Defina a função Lambda para processar a mensagem do SQS.
4. **Permissões IAM:** Conceda permissões para acessar o S3, enviar mensagens para o SQS e invocar a Lambda.

---

## Contribuição

- Faça um fork do projeto.
- Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
- Realize o commit das suas mudanças (`git commit -m 'Adiciona nova feature'`).
- Envie para o repositório remoto (`git push origin feature/nova-feature`).
- Abra um Pull Request.

---
