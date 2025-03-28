import requests
from requests.auth import HTTPDigestAuth

# Configurações do servidor
SERVER_HOST = "192.168.1.108"  # Substitua pelo IP do seu dispositivo
SERVER_PORT = "80"  # Porta padrão HTTP
BASE_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"

# Configurações do endpoint
ENDPOINT = "/cgi-bin/magicBox.cgi"
ACTION = "getLanguageCaps"

# Configurações de autenticação
AUTH_USERNAME = "admin"
AUTH_PASSWORD = "admin123"  # Substitua pela senha correta
AUTH_REALM = "Device_00408CA5EA04"

# Configurações do cliente
USER_AGENT = "client/1.0"

def get_language_caps():
    """
    Função para obter as configurações de idioma do dispositivo
    """
    # Monta a URL completa
    url = f"{BASE_URL}{ENDPOINT}"
    
    # Define os parâmetros da requisição
    params = {
        "action": ACTION
    }
    
    # Define os headers
    headers = {
        "User-Agent": USER_AGENT,
        "Content-Length": "0"
    }
    
    # Configuração da autenticação digest
    auth = HTTPDigestAuth(AUTH_USERNAME, AUTH_PASSWORD)
    
    try:
        # Faz a requisição GET com autenticação digest
        response = requests.get(
            url, 
            params=params,
            headers=headers,
            auth=auth
        )
        
        # Verifica se a requisição foi bem sucedida
        if response.status_code == 200:
            print("Conexão bem sucedida!")
            return response.json()
        else:
            print(f"Erro na requisição: Status code {response.status_code}")
            print(f"Resposta do servidor: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None

def print_connection_info():
    """
    Função para imprimir as informações de conexão
    """
    print("\nInformações de conexão:")
    print(f"Servidor: {SERVER_HOST}:{SERVER_PORT}")
    print(f"Endpoint: {ENDPOINT}")
    print(f"Ação: {ACTION}")
    print(f"Usuário: {AUTH_USERNAME}")
    print(f"Realm: {AUTH_REALM}")
    print(f"User Agent: {USER_AGENT}\n")

if __name__ == "__main__":
    # Mostra as informações de conexão
    print_connection_info()
    
    # Executa a requisição
    result = get_language_caps()
    
    # Mostra o resultado
    if result:
        print("\nResposta da requisição:")
        print(result)
