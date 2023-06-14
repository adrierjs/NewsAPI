import unittest
from unittest.mock import MagicMock
from scr.integrationGmail import sendEmailNews
from dotenv import load_dotenv
from scr.functions.template.readHTML import read_html_file
from scr.functions.newsAPI.dataFormatingNews import listNews
from scr.functions.newsAPI.integrationDataBaseNewsAPI import list_emails
import os

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD
template = read_html_file('../functions/template/template.html')

# Mocking the SMTP class
class MockSMTP:
    def __init__(self, *args, **kwargs):
        pass

    def send(self, *args, **kwargs):
        pass

class TestIntegrationGmail(unittest.TestCase):

    def test_sendEmailNews(self):
        load_dotenv()
        PASSWORD = os.getenv('PASSWORD')
        sender_email = 'dadosclimaticos.uepb@gmail.com'
        sender_password = PASSWORD
        template = read_html_file('../functions/template/template.html')

        # Mocking the SMTP instance
        mock_smtp = MockSMTP()

        # Mocking the send method of the SMTP instance
        mock_send = MagicMock()
        mock_smtp.send = mock_send

        with unittest.mock.patch('scr.integrationGmail.yagmail.SMTP', return_value=mock_smtp):
            sendEmailNews(listNews, list_emails, sender_email, sender_password, template)

        mock_send.assert_called_once()

if __name__ == '__main__':
    unittest.main()
