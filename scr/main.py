import os
from scr.functions.adivisor_api import advisor_API, convert_data
from dotenv import load_dotenv
# from scr.functions.send_email import init


load_dotenv() #Função para carregar as variáveis do arquivo .env
TOKEN = os.getenv('TOKEN')
APIKeyNewsAPI = os.getenv('APIKeyNewsAPI')
paramts_city_id = {
    "name": "Patos",
    "state": "PB",
    "token": TOKEN
}
paramts = {
    "token": TOKEN
}

paramtsNewsAPI = {
    "country": "br",
    "apiKey" : APIKeyNewsAPI,
    "category":"technology"
}
def chamar_API():
    data = advisor_API.fetch_city_id(paramts_city_id)

    list_city = []
    for i in range(len(data)):
        id = data[i]['id']
        list_city.append(advisor_API.meteorological_data(id, paramts))

    data_json = {}
    data_json = convert_data.format_data(list_city)
    return data_json

# json_string = json.dumps(chamar_API(),ensure_ascii=False) #Colocar aspas duplas nos atributos do dicionario
# print(json_string

# print(chamar_API())

# print(result)
#,'jennyfer.rocha','gabriel.lira','ronildo.lima','elder.andrare'













