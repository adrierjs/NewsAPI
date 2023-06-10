import os
import unittest
import psycopg2
from dotenv import load_dotenv

load_dotenv()

MAINTENANCE_DATABASE = os.getenv('MAINTENANCE_DATABASE')
USER_NAME = os.getenv('USER_NAME')
PASSWORD_DATABASE = os.getenv('PASSWORD_DATABASE')


class TestDatabaseConnection(unittest.TestCase):

    def test_database_connection(self):
        try:
            connection = psycopg2.connect(
                host="silly.db.elephantsql.com",
                port=5432,
                database=MAINTENANCE_DATABASE,
                user=USER_NAME,
                password=PASSWORD_DATABASE
            )
            cursor = connection.cursor()
            self.assertIsNotNone(connection)
            self.assertIsNotNone(cursor)
            print("Conexão estabelecida com sucesso!")
        except (Exception, psycopg2.Error) as error:
            self.fail("Erro ao conectar ao PostgreSQL: " + str(error))


if __name__ == '__main__':
    unittest.main()
