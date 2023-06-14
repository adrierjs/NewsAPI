import os
import unittest
from dotenv import load_dotenv
from datetime import date

class TestAPIParams(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.APIKeyNewsAPI = os.getenv('APIKeyNewsAPI')
        self.date_actual = date.today()

    def test_api_key_not_empty(self):
        self.assertIsNotNone(self.APIKeyNewsAPI, "A chave APIKeyNewsAPI não pode ser nula.")

    def test_params_news_api(self):
        paramsNewsAPI = {
            "apiKey": self.APIKeyNewsAPI,
            "q": "tecnologia",
            "language": 'pt',
            "pageSize": 10,
            "sortBy": 'popularity',
            "to": self.date_actual,
            "from": self.date_actual
        }

        self.assertEqual(paramsNewsAPI["q"], "tecnologia", "O valor da chave 'q' não corresponde.")
        self.assertEqual(paramsNewsAPI["language"], "pt", "O valor da chave 'language' não corresponde.")
        self.assertEqual(paramsNewsAPI["pageSize"], 10, "O valor da chave 'pageSize' não corresponde.")
        self.assertEqual(paramsNewsAPI["sortBy"], "popularity", "O valor da chave 'sortBy' não corresponde.")
        self.assertEqual(paramsNewsAPI["to"], self.date_actual, "O valor da chave 'to' não corresponde.")
        self.assertEqual(paramsNewsAPI["from"], self.date_actual, "O valor da chave 'from' não corresponde.")

if __name__ == '__main__':
    unittest.main()
