from cassandra.cluster import Cluster
import main
import uuid
# Cria um objeto de cluster Cassandra e se conecta
cluster = Cluster(['localhost'])
session = cluster.connect('dados_climaticos')

id = uuid.uuid1()
# Consulta os dados
query = f"INSERT INTO dados_clima (id, id_cidade, nome, estado, pais, temperatura, humidade, condicao, sensacao_termica, dia) " \
        f"VALUES ({id}, {main.data_json['id_cidade']}, '{main.data_json['nome']}', '{main.data_json['estado']}', " \
        f"'{main.data_json['pais']}', {main.data_json['temperatura']}, {main.data_json['humidade']}, " \
        f"'{main.data_json['condicao']}', {main.data_json['sensacao_termica']}, '{main.data_json['dia']}');"
session.execute(query)

list_data = []
query = 'SELECT * FROM dados_clima '
dados = (session.execute(query))
for i in dados:
        (list_data.append(i))

linhas_ordenadas = sorted(list_data, key=lambda linha: linha.dia)
for linha in linhas_ordenadas:
    print(linha)
