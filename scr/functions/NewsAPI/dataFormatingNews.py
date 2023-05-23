from scr.functions.NewsAPI.integrationNewsAPI import newsGeneric
def formatingNewsAPI(result):
    lista_news = []
    for row in result['articles']:
        author = row['author']
        title = row['title']
        url = row['url']
        news_string = f'Autor: {author}\nTítulo: {title}\nURL: {url}\n\n'
        lista_news.append(news_string)
    return ''.join(lista_news)

listNews = formatingNewsAPI(newsGeneric)

