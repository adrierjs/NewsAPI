from cassandra.cluster import Cluster

# Cria um objeto de cluster Cassandra e se conecta
cluster = Cluster(['localhost'])
session = cluster.connect()

# Consulta os dados
# result_set = session.execute("SELECT * FROM curso_cassandra.alunos;")
# keyspaces = session.execute("DESCRIBE KEYSPACES;")

# Fecha a conexão
# cluster.shutdown()
