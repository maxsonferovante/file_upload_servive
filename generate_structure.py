import os

# Defina a estrutura de diretórios e arquivos
structure = {
    "app": [
        "main.py",
        "api/v1/__init__.py",
        "api/v1/upload_router.py",
        "api/v1/status_router.py",
        "api/v1/schemas.py",
        "api/__init__.py",
        "core/__init__.py",
        "core/config.py",
        "core/exceptions.py",
        "domain/__init__.py",
        "domain/models/__init__.py",
        "domain/models/file_model.py",
        "domain/repositories/__init__.py",
        "domain/repositories/file_repository.py",
        "usecases/__init__.py",
        "usecases/upload_file.py",
        "usecases/confirm_upload.py",
        "usecases/update_status.py",
        "services/__init__.py",
        "services/s3_service.py",
        "services/sqs_service.py",
        "infrastructure/__init__.py",
        "infrastructure/database.py",
        "infrastructure/file_repository_impl.py"
    ],
    "tests": [
        "__init__.py",
        "test_upload.py",
        "test_confirm_upload.py",
        "test_update_status.py"
    ],
    ".": [
        "Dockerfile",
        "docker-compose.yml",
        "requirements.txt",
    ]
}
# Função para criar diretórios e arquivos
def create_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        
        # Cria os diretórios
        os.makedirs(folder_path, exist_ok=True)
        
        # Cria os arquivos em cada diretório
        for file in files:
            file_path = os.path.join(folder_path, file)
            
            # Garante que o diretório para o arquivo existe
            file_dir = os.path.dirname(file_path)
            os.makedirs(file_dir, exist_ok=True)
            
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write("")  # Arquivo vazio
                print(f"Arquivo criado: {file_path}")
            else:
                print(f"Arquivo já existe: {file_path}")


# Executa a criação da estrutura
if __name__ == "__main__":
    base_path = os.getcwd()  # Diretório atual
    create_structure(base_path, structure)
    print("\nEstrutura de projeto criada com sucesso!")
