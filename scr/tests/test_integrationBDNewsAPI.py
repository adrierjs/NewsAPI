import unittest
from unittest.mock import patch, MagicMock
import scr.connect_bd as connect_bd

class TestIntegrationBDNewsAPI(unittest.TestCase):

    @patch('scr.connect_bd.psycopg2.connect')
    def test_fetch_emails(self, mock_connect):
        # Simula o resultado retornado pela consulta SQL
        mock_result = [
            (1, 'John', 'john@example.com'),
            (2, 'Jane', 'jane@example.com')
        ]

        # Cria um objeto mock para o cursor
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = mock_result

        # Substitui a chamada para psycopg2.connect()
        mock_connection = mock_connect.return_value.__enter__.return_value
        mock_connection.cursor.return_value = mock_cursor

        # Executa a consulta SQL
        mock_cursor.execute.return_value = None
        connect_bd.cursor = mock_cursor  # Substitui o objeto cursor pelo objeto mock_cursor
        connect_bd.cursor.execute('select * from app_django_news_registro')
        result = connect_bd.cursor.fetchall()

        # Verifica se o método .execute() foi chamado corretamente
        mock_cursor.execute.assert_called_once_with('select * from app_django_news_registro')

        # Verifica se o método .fetchall() foi chamado corretamente
        mock_cursor.fetchall.assert_called_once()

        # Verifica se a lista de e-mails foi preenchida corretamente
        expected_emails = ['john@example.com', 'jane@example.com']
        actual_emails = [row[2] for row in result]
        self.assertEqual(actual_emails, expected_emails)

if __name__ == '__main__':
    unittest.main()
