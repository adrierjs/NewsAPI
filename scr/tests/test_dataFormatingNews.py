import unittest
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

class TestFormatingNewsAPI(unittest.TestCase):
    def test_formatingNewsAPI(self):
        # Dados de teste
        result = newsGeneric

        # Chamada da função a ser testada
        listNews = formatingNewsAPI(result)

        # Verificações
        self.assertIsInstance(listNews, list)
        self.assertGreater(len(listNews), 0)
        for news in listNews:
            self.assertIsInstance(news, dict)
            self.assertIn('author', news)
            self.assertIn('title', news)
            self.assertIn('url', news)

if __name__ == '__main__':
    unittest.main()
