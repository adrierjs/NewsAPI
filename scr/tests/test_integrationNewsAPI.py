import requests
import unittest
from scr.functions.newsAPI.autenticateNewsAPI import paramtsNewsAPI


def topHeadlines(params):
    urlTopHeadlines = 'https://newsapi.org/v2/everything'
    response = requests.get(urlTopHeadlines, params=params)
    if response.ok:
        data = response.json()
        return data
    else:
        raise Exception(response.status_code)


class TestTopHeadlines(unittest.TestCase):
    def test_successful_request(self):
        params = paramtsNewsAPI
        result = topHeadlines(params)
        self.assertIsNotNone(result)
        self.assertIn('articles', result)

    def test_failed_request(self):
        params = {'invalid_param': 'value'}
        with self.assertRaises(Exception):
            topHeadlines(params)


if __name__ == '__main__':
    unittest.main()
