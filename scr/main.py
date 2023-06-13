from scr.integrationGmail import sendEmailNews
from dotenv import load_dotenv
from functions.NewsAPI.dataFormatingNews import listNews
from functions.integrationBDNewsAPI import list_emails
import os

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