from jinja2 import Environment, FileSystemLoader

# Crie o ambiente Jinja2
env = Environment(loader=FileSystemLoader('.'))

# Defina a variável que você deseja passar para o HTML
nome = "Adrier"
sobrenome = "José"

# Renderize o template HTML
template = env.get_template('template.html')
html_output = template.render(nome=nome, sobrenome=sobrenome)

# Exiba o resultado
print(html_output)
