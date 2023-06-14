import os
from dotenv import load_dotenv

load_dotenv() #Função para carregar as variáveis do arquivo .env
# TOKEN = os.getenv('TOKEN')
APIKeyNewsAPI = os.getenv('APIKeyNewsAPI')
paramtsNewsAPI = {
    "country": "br",
    "apiKey" : APIKeyNewsAPI,
    "category":"technology",
    "pageSize": 10
}













