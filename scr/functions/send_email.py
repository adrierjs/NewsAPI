import yagmail
from dotenv import load_dotenv
from NewsAPI.dataFormatingNews import listNews
import os

def sendEmailNews(listNews, emails,sender_email, sender_password):
    subject = 'Newlatter Computing - UEPB'
    for i in range(len(emails)):
        dominio = '@aluno.uepb.edu.br'
        recipient = emails[i] + dominio
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(to=recipient, subject=subject, contents=listNews)
        print(f"Email enviado para {recipient}")


load_dotenv()
PASSWORD = os.getenv('PASSWORD')
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD
emails = ['adrier.santos']
sendEmailNews(listNews, emails,sender_email, sender_password)






