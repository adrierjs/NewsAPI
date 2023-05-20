import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
MAINTENANCE_DATABASE = os.getenv('MAINTENANCE_DATABASE')
USER_NAME = os.getenv('USER_NAME')
PASSWORD_DATABASE = os.getenv('PASSWORD_DATABASE')



try:
    connection = psycopg2.connect(
        host="silly.db.elephantsql.com",
        port=5432,
        database=MAINTENANCE_DATABASE,
        user=USER_NAME,
        password=PASSWORD_DATABASE
    )
    cursor = connection.cursor()
    print("Conexão estabelecida com sucesso!")
except (Exception, psycopg2.Error) as error:
    print("Erro ao conectar ao PostgreSQL:", error)


