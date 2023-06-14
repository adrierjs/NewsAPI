import unittest
from unittest.mock import patch
from scr.integrationGmail import sendEmailNews, remove_extra_spaces

class TestSendEmailNews(unittest.TestCase):
    def test_sendEmailNews(self):
        listNews = [
            {'title': 'News 1', 'description': 'Description 1', 'source_name': 'Source 1', 'url': 'http://example.com/news1', 'publishedAt': '2023-06-01'},
            {'title': 'News 2', 'description': 'Description 2', 'source_name': 'Source 2', 'url': 'http://example.com/news2', 'publishedAt': '2023-06-02'},
            {'title': 'News 3', 'description': 'Description 3', 'source_name': 'Source 3', 'url': 'http://example.com/news3', 'publishedAt': '2023-06-03'}
        ]
        emails = ['recipient1@example.com', 'recipient2@example.com']
        sender_email = 'sender@example.com'
        sender_password = 'password'
        template = '<tr><td>Title: {title}</td><td>Description: {description}</td><td>Source: {source_name}</td><td>URL: {url}</td><td>Published At: {publishedAt}</td></tr>'

        with patch('yagmail.SMTP') as mock_smtp:
            instance = mock_smtp.return_value

            sendEmailNews(listNews, emails, sender_email, sender_password, template)

            mock_smtp.assert_called_once_with(sender_email, sender_password)
            expected_contents = '<table><tr><td>Title: News 1</td><td>Description: Description 1</td><td>Source: Source 1</td><td>URL: http://example.com/news1</td><td>Published At: 2023-06-01</td></tr><tr><td>Title: News 2</td><td>Description: Description 2</td><td>Source: Source 2</td><td>URL: http://example.com/news2</td><td>Published At: 2023-06-02</td></tr><tr><td>Title: News 3</td><td>Description: Description 3</td><td>Source: Source 3</td><td>URL: http://example.com/news3</td><td>Published At: 2023-06-03</td></tr></table>'
            instance.send.assert_called_once_with(to=emails, subject='Newsletter Computing - UEPB', contents=expected_contents)

    def test_remove_extra_spaces(self):
        text_with_extra_spaces = '  This   is  a    test.  '
        expected_text = 'This is a test.'
        cleaned_text = remove_extra_spaces(text_with_extra_spaces)
        self.assertEqual(cleaned_text, expected_text, "A função remove_extra_spaces não removeu corretamente os espaços extras.")

if __name__ == '__main__':
    unittest.main()
