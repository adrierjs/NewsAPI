import os
from dotenv import load_dotenv
from datetime import date

load_dotenv() #Função para carregar as variáveis do arquivo .env
APIKeyNewsAPI = os.getenv('APIKeyNewsAPI')
date_actual = date.today()

paramtsNewsAPI = {
    "apiKey" : APIKeyNewsAPI,
    "q":"tecnologia",
    "language": 'pt',
    "pageSize": 10,
    "sortBy": 'popularity',
    "to": date_actual,
    "from": date_actual
}













