import yagmail
from scr.main import *
from dotenv import load_dotenv
import os
from jinja2 import Environment, FileSystemLoader

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
# Configuração da conta de e-mail
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD

# Obtém o diretório do script atual
base_dir = os.path.dirname(os.path.abspath(__file__))
# Define o diretório do template
template_dir = os.path.join(base_dir, 'scr', '..')
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('template.html')

# Configuração do destinatário e mensagem
emails = ['adrier.santos', 'ronildo.junior', 'gabriel.lira','elder.andrade']

# Cria o objeto yagmail e envia o e-mail

for email in emails:
    dados = chamar_API()
    nome = email
    # Função para adicionar variáveis dinâmicas no HTML
    html_output = template.render(nome=nome, dados=dados)
    body = html_output
    subject = 'Dados climáticos - Patos - PB'
    dominio = '@aluno.uepb.edu.br'
    recipient = email + dominio
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(to=recipient, subject=subject, contents=body)
    print(f"Email enviado para {recipient}")
