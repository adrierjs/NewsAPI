import yagmail
from scr.main import *
from dotenv import load_dotenv
import os
from jinja2 import Environment, FileSystemLoader


load_dotenv()
PASSWORD = os.getenv('PASSWORD')
# Configuração da conta de e-mail
# sender_email = 'dadosclimaticos.uepb@gmail.com'
# sender_password = PASSWORD

# env = Environment(loader=FileSystemLoader('.'))
# template = env.get_template('template.html')


# Configuração do destinatário e mensagem
emails = ['adrier.santos', 'ronildo.junior', 'gabriel.lira','elder.andrade']
# recipient = 'adrier.santos@aluno.uepb.edu.br'

# Cria o objeto yagmail e envia o e-mail

for i in range (len(emails)):
    dados = chamar_API()
    nome = emails[i]
    #Funcao para adicionar varíaveis dinâmicas no html
    html_output = template.render(nome=nome, dados=dados)
    body = dados
    subject = f'Dados climáticos - Patos - PB'
    dominio = '@aluno.uepb.edu.br'
    recipient = emails[i]+dominio
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(to=recipient, subject=subject, contents=body)
    print(f"Email enviado para {recipient}")


