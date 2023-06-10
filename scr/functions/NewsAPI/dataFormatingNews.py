from scr.functions.NewsAPI.integrationNewsAPI import newsGeneric
def formatingNewsAPI(result):
    lista_dicionarios = []
    for row in result['articles']:
        author = row['author']
        title = row['title']
        url = row['url']
        dicionario = {'author': author, 'title': title, 'url': url}
        lista_dicionarios.append(dicionario)
    return lista_dicionarios

listNews = formatingNewsAPI(newsGeneric)
print(listNews)
