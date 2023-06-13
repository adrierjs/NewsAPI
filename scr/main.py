import yagmail
from dotenv import load_dotenv
from functions.NewsAPI.dataFormatingNews import listNews
from functions.integrationBDNewsAPI import list_emails
import os
import re

def remove_extra_spaces(text):
    # Remove espaços extras e quebras de linha
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def sendEmailNews(listNews, emails, sender_email, sender_password, template):
    subject = 'Newsletter Computing - UEPB'
    yag = yagmail.SMTP(sender_email, sender_password)
    contents = "<table>"
    for news in listNews:
        formatted_news = template.format(title=news['title'], author=news['author'], url=news['url'])
        formatted_news = remove_extra_spaces(formatted_news)
        contents += formatted_news
    contents += "</table>"
    yag.send(to=emails, subject=subject, contents=contents)
    print("E-mail enviado para todos os destinatários")

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD
template = """<tr>
  <td>
    <h1>{title}</h1>
    <h4>Autor:<strong> {author}</strong></h4>
    <p>Para ler mais, acesse: <a href="{url}">Ler mais</a></p>
  </td>
</tr>"""
sendEmailNews(listNews, list_emails, sender_email, sender_password, template)
