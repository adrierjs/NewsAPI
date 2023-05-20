from scr.connect_bd import *
from scr.main import *

def insert_data(current_weather_data):
    comando_sql = """
        INSERT INTO dados_clima_diarios (id_cidade, nome, estado, pais, temperatura, direcao_vento, velocidade_vento, humidade, condicao, pressao, sensacao_termica, data_atual)
        VALUES ({id_cidade}, '{nome}', '{estado}', '{pais}', {temperatura}, '{direcao_vento}', {velocidade_vento}, {humidade}, '{condicao}', {pressao}, {sensacao_termica}, '{data_atual}')
    """.format(**current_weather_data)
    try:
        cursor.execute(comando_sql)
        connection.commit()
        print("Dados inseridos com sucesso!")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao inserir dados:", error)

def search_data():
    pass


current_weather_data = chamar_API()

# insert_data(current_weather_data)

cursor.execute('select * from dados_clima_diarios')
result = cursor.fetchall()

for row in result:
    print(row)
