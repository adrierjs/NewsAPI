from scr.functions.NewsAPI.integrationNewsAPI import newsGeneric
# def formatingNewsAPI(result):
#     lista_news = []
#     for row in result['articles']:
#         author = row['author']
#         title = row['title']
#         url = row['url']
#         news_string = f'Autor: {author}\nTítulo: {title}\nURL: {url}\n'
#         lista_news.append(news_string)
#     # return ''.join(lista_news)
#     return lista_news
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

