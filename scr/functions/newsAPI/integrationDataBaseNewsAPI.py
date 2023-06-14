from scr.database.connectDataBase import *

cursor.execute('select * from app_django_news_registro')
result = cursor.fetchall()

list_emails = []
for row in result:
    list_emails.append(row[2])
