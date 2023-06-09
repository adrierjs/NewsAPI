import yagmail

# Configurações do servidor de e-mail
smtp_host = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'seu_email@gmail.com'
smtp_password = 'sua_senha'

# Criar o objeto yagmail
yag = yagmail.SMTP(smtp_username, smtp_password)

# Dados para renderizar o template HTML
titulo1 = 'Título da Notícia 1'
autor1 = 'Autor da Notícia 1'
url1 = 'https://exemplo.com/noticia1'

titulo2 = 'Título da Notícia 2'
autor2 = 'Autor da Notícia 2'
url2 = 'https://exemplo.com/noticia2'

# ... repetir para as demais notícias

# Configurar as variáveis no contexto do template
noticias = [
    {'titulo': titulo1, 'autor': autor1, 'url': url1},
    {'titulo': titulo2, 'autor': autor2, 'url': url2},
    # ... adicionar as demais notícias
]

# Carregar o template HTML
template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Email com Notícias</title>
</head>
<body>
  <h1>Notícias</h1>
  {% for noticia in noticias %}
  <h2>{{ noticia['titulo'] }}</h2>
  <p>Autor: {{ noticia['autor'] }}</p>
  <p>Para ler mais, acesse: <a href="{{ noticia['url'] }}">Ler mais</a></p>
  <hr>
  {% endfor %}
</body>
</html>
"""

# Renderizar o template com as variáveis
html = yag.render(template, noticias=noticias)

# Enviar o e-mail
yag.send(
    to='destinatario@gmail.com',
    subject='Notícias',
    contents=html
)

print('E-mail enviado com sucesso!')
