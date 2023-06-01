from scr.connect_bd import *

cursor.execute('select * from tabela_usuarios')
result = cursor.fetchall()

for row in result:
    print(row)
