from scr.integrationGmail import sendEmailNews
from dotenv import load_dotenv
from scr.functions.template.readHTML import read_html_file
from functions.NewsAPI.dataFormatingNews import listNews
from functions.integrationBDNewsAPI import list_emails
import os

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD
template = read_html_file('functions/template/template.html')

sendEmailNews(listNews, list_emails, sender_email, sender_password, template)