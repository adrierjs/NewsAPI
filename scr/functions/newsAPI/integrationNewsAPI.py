import requests
from scr.functions.newsAPI.autenticateNewsAPI import paramtsNewsAPI
def topHeadlines(params):
    urlTopHeadines = "https://newsapi.org/v2/top-headlines"
    response = requests.get(urlTopHeadines, params=params)
    if response.ok:
        data = response.json()
        return data
    else:
        raise Exception(requests.status_codes)

newsGeneric = topHeadlines(paramtsNewsAPI)