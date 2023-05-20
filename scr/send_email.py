import yagmail
import main
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.getenv('PASSWORD')
# Configuração da conta de e-mail
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD

# Configuração do destinatário e mensagem
emails = ['adrier.santos']
# recipient = 'adrier.santos@aluno.uepb.edu.br'



# Cria o objeto yagmail e envia o e-mail

for i in range (len(emails)):
    dados = main.chamar_API()
    body = f'{dados}'
    subject = f'Dados climáticos - Patos - PB'
    dominio = '@aluno.uepb.edu.br'
    recipient = emails[i]+dominio
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(to=recipient, subject=subject, contents=body)
    print(f"Email enviado para {recipient}")
    print(body)


