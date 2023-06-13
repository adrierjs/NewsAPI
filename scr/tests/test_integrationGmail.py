import unittest
from unittest.mock import patch
from scr.integrationGmail import sendEmailNews

class TestSendEmailNews(unittest.TestCase):

    def test_sendEmailNews(self):
        listNews = [
            {'title': 'News 1', 'author': 'Author 1', 'url': 'http://example.com/news1'},
            {'title': 'News 2', 'author': 'Author 2', 'url': 'http://example.com/news2'},
            {'title': 'News 3', 'author': 'Author 3', 'url': 'http://example.com/news3'}
        ]
        emails = ['recipient1@example.com', 'recipient2@example.com']
        sender_email = 'sender@example.com'
        sender_password = 'password'
        template = '<tr><td>Title: {title}</td><td>Author: {author}</td><td>URL: {url}</td></tr>'

        with patch('yagmail.SMTP') as mock_smtp:
            instance = mock_smtp.return_value

            sendEmailNews(listNews, emails, sender_email, sender_password, template)

            mock_smtp.assert_called_once_with(sender_email, sender_password)
            instance.send.assert_called_once_with(to=emails, subject='Newsletter Computing - UEPB', contents='<table><tr><td>Title: News 1</td><td>Author: Author 1</td><td>URL: http://example.com/news1</td></tr><tr><td>Title: News 2</td><td>Author: Author 2</td><td>URL: http://example.com/news2</td></tr><tr><td>Title: News 3</td><td>Author: Author 3</td><td>URL: http://example.com/news3</td></tr></table>')

if __name__ == '__main__':
    unittest.main()
