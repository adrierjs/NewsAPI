from scr.connect_bd import *

cursor.execute('SELECT * FROM "public"."app_django_news_registro"')
result = cursor.fetchall()

list_emails = []
for row in result:
    list_emails.append(row[2])
