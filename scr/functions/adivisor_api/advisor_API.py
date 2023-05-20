import requests


def fetch_city_id(params):
    url_city_id = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=&state=&token='
    response = requests.get(url_city_id, params=params)
    if response.ok:
        data = response.json()
        return data
    else:
        raise Exception(requests.status_codes)


def meteorological_data(city_id, paramts):
    url = f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current?token='
    response = requests.get(url, params=paramts)
    if response.ok:
        return response.json()
    else:
        return Exception(requests.status_codes)

