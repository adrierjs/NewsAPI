import unittest
from unittest.mock import patch, MagicMock
from scr.integrationGmail import sendEmailNews, remove_extra_spaces

class TestMain(unittest.TestCase):
    @patch('main.yagmail.SMTP')
    def test_sendEmailNews(self, mock_smtp):
        # Dados de exemplo
        listNews = [
            {'title': 'Notícia 1', 'author': 'Autor 1', 'url': 'https://example.com/news1'},
            {'title': 'Notícia 2', 'author': 'Autor 2', 'url': 'https://example.com/news2'}
        ]
        emails = ['email1@example.com', 'email2@example.com']
        sender_email = 'sender@example.com'
        sender_password = 'password'
        template = """<tr>
          <td>
            <h1>{title}</h1>
            <h4>Autor:<strong> {author}</strong></h4>
            <p>Para ler mais, acesse: <a href="{url}">Ler mais</a></p>
          </td>
        </tr>"""

        # Executa a função de envio de email
        sendEmailNews(listNews, emails, sender_email, sender_password, template)

        # Verifica se a função yag.send foi chamada corretamente
        mock_smtp.return_value.send.assert_called_once_with(to=emails, subject='Newsletter Computing - UEPB', contents=MagicMock())

    def test_remove_extra_spaces(self):
        # Texto de exemplo com espaços extras
        text = '   Hello    World   '

        # Executa a função de remoção de espaços extras
        result = remove_extra_spaces(text)

        # Verifica se os espaços extras foram removidos corretamente
        self.assertEqual(result, 'Hello World')

if __name__ == '__main__':
    unittest.main()
