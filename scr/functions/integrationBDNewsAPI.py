from scr.connect_bd import *

cursor.execute('select * from tabela_usuarios')
result = cursor.fetchall()

list_emails = []
for row in result:
    list_emails.append(row[2])
