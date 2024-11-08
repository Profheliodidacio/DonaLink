# settings.py

import toml

# Carregar configurações do arquivo TOML
def load_config():
    config = toml.load('config.toml')
    
    # Retorna as configurações carregadas
    return config

# Configurações principais do aplicativo
config = load_config()

# Configurações de ambiente (Exemplo: desenvolvimento, produção, etc)
ENVIRONMENT = config.get('app', {}).get('environment', 'development')

# Configurações do app
APP_NAME = config['app']['name']
APP_VERSION = config['app']['version']
APP_DESCRIPTION = config['app']['description']

# Configurações de API
API_BASE_URL = config['api']['base_url']
CHATBOT_ENDPOINT = config['api']['chatbot_endpoint']

# Configurações de doações
MIN_DONATION = config['donations']['minimum_donation']
MAX_DONATION = config['donations']['maximum_donation']
CURRENCY = config['donations']['currency']

# Configurações de banco de dados
DB_HOST = config['database']['host']
DB_PORT = config['database']['port']
DB_USER = config['database']['user']
DB_PASSWORD = config['database']['password']
DB_NAME = config['database']['database_name']

# Configurações de tema
PRIMARY_COLOR = config['theme']['primary_color']
SECONDARY_COLOR = config['theme']['secondary_color']
FONT = config['theme']['font']

# Configurações de autenticação
LOGIN_ENABLED = config['authentication']['enable_login']
MAX_LOGIN_ATTEMPTS = config['authentication']['max_login_attempts']

# Informações de contato
CONTACT_EMAIL = config['contact']['email']
CONTACT_PHONE = config['contact']['phone']

# Funções para acessar configurações de forma simples
def get_db_connection_string():
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

