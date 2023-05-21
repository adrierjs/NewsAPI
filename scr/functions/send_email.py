import yagmail
from scr.main import *
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.getenv('PASSWORD')
# Configuração da conta de e-mail
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD

# Configuração do destinatário e mensagem
emails = ['adrier.santos', 'ronildo.junior', 'gabriel.lira','elder.andrade']

# Cria o objeto yagmail e envia o e-mail

for email in emails:
    body = chamar_API()
    nome = email
    # Função para adicionar variáveis dinâmicas no HTML
    subject = 'Dados climáticos - Patos - PB'
    dominio = '@aluno.uepb.edu.br'
    recipient = email + dominio
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(to=recipient, subject=subject, contents=body)
    print(f"Email enviado para {recipient}")
