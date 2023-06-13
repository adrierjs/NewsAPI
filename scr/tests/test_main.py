import unittest
from unittest.mock import patch
from scr.integrationGmail import sendEmailNews
import os
class TestIntegrationGmail(unittest.TestCase):

    @patch('scr.integrationGmail.yagmail.SMTP')
    def test_sendEmailNews(self, mock_smtp):
        from dotenv import load_dotenv
        from scr.functions.NewsAPI.dataFormatingNews import listNews
        from scr.functions.integrationBDNewsAPI import list_emails

        load_dotenv()
        PASSWORD = os.getenv('PASSWORD')
        sender_email = 'dadosclimaticos.uepb@gmail.com'
        sender_password = PASSWORD
        template = """<tr>
          <td>
            <h1>{title}</h1>
            <h4>Autor:<strong> {author}</strong></h4>
            <p>Para ler mais, acesse: <a href="{url}">Ler mais</a></p>
          </td>
        </tr>"""

        sendEmailNews(listNews, list_emails, sender_email, sender_password, template)

        mock_smtp.assert_called_once_with(sender_email, sender_password)
        instance = mock_smtp.return_value
        instance.send.assert_called_once()

if __name__ == '__main__':
    unittest.main()
