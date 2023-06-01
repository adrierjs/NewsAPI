import yagmail
from dotenv import load_dotenv
from NewsAPI.dataFormatingNews import listNews
from integrationBDNewsAPI import list_emails
import os

def sendEmailNews(listNews, emails,sender_email, sender_password):
    subject = 'Newlatter Computing - UEPB'
    for i in range(len(emails)):
        recipient = emails[i]
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(to=recipient, subject=subject, contents=listNews)
        print(f"Email enviado para {recipient}")


load_dotenv()
PASSWORD = os.getenv('PASSWORD')
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD
sendEmailNews(listNews, list_emails,sender_email, sender_password)






