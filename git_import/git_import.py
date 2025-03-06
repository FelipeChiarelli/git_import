import requests
import base64
import os
import importlib.util

def git_import(username, repo_name, file_path, token, encoding='utf-8', import_as_module=True):
    """
    Baixa um arquivo Python de um repositório GitHub (público ou privado) e o importa como módulo, se desejado.

    Parâmetros:
    - username (str): Nome do usuário ou organização no GitHub.
    - repo_name (str): Nome do repositório.
    - file_path (str): Caminho do arquivo dentro do repositório.
    - token (str): Token de autenticação do GitHub (necessário para repositórios privados).
    - encoding (str, opcional): Codificação do arquivo. Padrão é 'utf-8'.
    - import_as_module (bool, opcional): Se True, importa o arquivo como módulo e retorna. Padrão é True.

    Retorna:
    - Se import_as_module=True, retorna o módulo importado.
    - Caso contrário, retorna o caminho do arquivo salvo.

    Exemplo de uso:
    
    python
    func = git_import("FelipeChiarelli", "PortfolioStatistics", "port_stats_V1_2.py", "seu_token")
    resultado = func.alguma_funcao()  # Chamar uma função do arquivo baixado
    """
    
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}"
    headers = {"Authorization": f"token {token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        file_content = response.json()["content"]
        decoded_content = base64.b64decode(file_content).decode(encoding)
        
        local_path = os.path.basename(file_path)
        with open(local_path, "w", encoding=encoding) as f:
            f.write(decoded_content)
        
        print(f"Arquivo {file_path} baixado com sucesso!")

        if import_as_module:
            module_name = os.path.splitext(local_path)[0]
            spec = importlib.util.spec_from_file_location(module_name, local_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"Módulo {module_name} importado com sucesso!")
            return module
        
        return local_path  
    else:
        print(f"Erro ao baixar o arquivo: {response.status_code}")
        print(response.text)
        return None