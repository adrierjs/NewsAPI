import requests
import os
from dotenv import load_dotenv

def fetch_city_id(params):
    url_city_id = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=&state=&token='
    response = requests.get(url_city_id, params=paramts_city_id)
    if response.ok:
        data = response.json()
        return data
    else:
        return f'Erro ao fazer request {response.status_code}'


def meteorological_data(city_id, paramts):
    url = f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current?token='
    response = requests.get(url, params=paramts)
    if response.ok:
        return response.json()
    else:
        return f'Erro na requisição! {response.status_code}'

load_dotenv()
TOKEN = os.getenv('TOKEN')



paramts_city_id = {
    "name": "Jardim do Seridó",
    "state": "RN",
    "token": TOKEN
}

data = fetch_city_id(paramts_city_id)

id = data[0]['id']
paramts = {
    "token":TOKEN
}

print(meteorological_data(id,paramts))


