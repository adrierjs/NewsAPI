import unittest
from scr.functions.newsAPI.integrationNewsAPI import newsGeneric
from datetime import datetime, timedelta

def formatingNewsAPI(result):
    lista_dicionarios = []
    for row in result['articles']:
        source_name = row['source']['name'] if 'source' in row and 'name' in row['source'] else ''
        title = row['title']
        url = row['url']
        description = row['description']
        publishedAt = row['publishedAt']
        publishedAt = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=3)
        publishedAt = publishedAt.strftime('%Y-%m-%d %H:%M')
        dicionario = {'title': title, 'description': description, 'source_name': source_name, 'url': url, 'publishedAt': publishedAt}
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
            self.assertIn('title', news)
            self.assertIn('description', news)
            self.assertIn('source_name', news)
            self.assertIn('url', news)
            self.assertIn('publishedAt', news)

if __name__ == '__main__':
    unittest.main()
