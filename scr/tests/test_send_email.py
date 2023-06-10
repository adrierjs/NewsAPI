import unittest
from unittest.mock import MagicMock
from scr.functions.send_email import sendEmailNews


class TestSendEmailNews(unittest.TestCase):

    def test_sendEmailNews(self):
        listNews = [{'author': 'TechTudo', 'title': 'Como descobrir senha do Wi-Fi a que você está conectado? Guia completo - TechTudo', 'url': 'https://news.google.com/rss/articles/CBMigAFodHRwczovL3d3dy50ZWNodHVkby5jb20uYnIvZ3VpYS8yMDIzLzA2L2NvbW8tZGVzY29icmlyLXNlbmhhLWRvLXdpLWZpLWEtcXVlLXZvY2UtZXN0YS1jb25lY3RhZG8tZ3VpYS1jb21wbGV0by1lZHNvZnR3YXJlcy5naHRtbNIBiwFodHRwczovL3d3dy50ZWNodHVkby5jb20uYnIvZ29vZ2xlL2FtcC9ndWlhLzIwMjMvMDYvY29tby1kZXNjb2JyaXItc2VuaGEtZG8td2ktZmktYS1xdWUtdm9jZS1lc3RhLWNvbmVjdGFkby1ndWlhLWNvbXBsZXRvLWVkc29mdHdhcmVzLmdodG1s?oc=5'}, {'author': 'Canaltech', 'title': 'Quanto vale a pena pagar pelo Moto E22? - Canaltech', 'url': 'https://news.google.com/rss/articles/CBMiUGh0dHBzOi8vY2FuYWx0ZWNoLmNvbS5ici9wcm9kdXRvcy9xdWFudG8tdmFsZS1hLXBlbmEtcGFnYXItcGVsby1tb3RvLWUyMi0yNTIxNjQv0gEA?oc=5'}, {'author': 'TecMundo', 'title': 'Com Far Cry 6 e mais jogos, Ubisoft+ está grátis por tempo limitado - TecMundo', 'url': 'https://news.google.com/rss/articles/CBMiWmh0dHBzOi8vd3d3LnRlY211bmRvLmNvbS5ici92b3hlbC8yNjUwMzItZmFyLWNyeS02LWpvZ29zLXViaXNvZnQtZ3JhdGlzLXRlbXBvLWxpbWl0YWRvLmh0bdIBAA?oc=5'}, {'author': 'MacMagazine', 'title': 'iOS/iPadOS 17, macOS Sonoma 14, watchOS 10… um resumão dos novos sistemas da Apple! - MacMagazine', 'url': 'https://news.google.com/rss/articles/CCAiC3h1MXJyRE8wbmRRmAEB?oc=5'}, {'author': 'Tecnoblog', 'title': 'Galaxy S22 Ultra de 256 GB está quase 50% mais barato que S23 Ultra nesta oferta com menor preço histórico – Tecnoblog - Tecnoblog', 'url': 'https://news.google.com/rss/articles/CBMikwFodHRwczovL3RlY25vYmxvZy5uZXQvYWNoYWRvcy8yMDIzLzA2LzA5L2dhbGF4eS1zMjItdWx0cmEtZGUtMjU2LWdiLWVzdGEtcXVhc2UtNTAtbWFpcy1iYXJhdG8tcXVlLXMyMy11bHRyYS1uZXN0YS1vZmVydGEtY29tLW1lbm9yLXByZWNvLWhpc3Rvcmljby_SAQA?oc=5'}, {'author': 'CartaCapital', 'title': 'Gigante brasileira de tecnologia entra na mira do MPT por coação de funcionários - CartaCapital', 'url': 'https://news.google.com/rss/articles/CBMie2h0dHBzOi8vd3d3LmNhcnRhY2FwaXRhbC5jb20uYnIvc29jaWVkYWRlL2dpZ2FudGUtYnJhc2lsZWlyYS1kZS10ZWNub2xvZ2lhLWVudHJhLW5hLW1pcmEtZG8tbXB0LXBvci1jb2FjYW8tZGUtZnVuY2lvbmFyaW9zL9IBf2h0dHBzOi8vd3d3LmNhcnRhY2FwaXRhbC5jb20uYnIvc29jaWVkYWRlL2dpZ2FudGUtYnJhc2lsZWlyYS1kZS10ZWNub2xvZ2lhLWVudHJhLW5hLW1pcmEtZG8tbXB0LXBvci1jb2FjYW8tZGUtZnVuY2lvbmFyaW9zL2FtcC8?oc=5'}, {'author': 'Adrenaline', 'title': 'Transmissão-N: evento brasileiro promete novidades para os donos do Nintendo Switch - Adrenaline', 'url': 'https://news.google.com/rss/articles/CBMid2h0dHBzOi8vd3d3LmFkcmVuYWxpbmUuY29tLmJyL2dhbWVzL3RyYW5zbWlzc2FvLW4tZXZlbnRvLWJyYXNpbGVpcm8tcHJvbWV0ZS1ub3ZpZGFkZXMtcGFyYS1vcy1kb25vcy1kby1uaW50ZW5kby1zd2l0Y2gv0gF7aHR0cHM6Ly93d3cuYWRyZW5hbGluZS5jb20uYnIvZ2FtZXMvdHJhbnNtaXNzYW8tbi1ldmVudG8tYnJhc2lsZWlyby1wcm9tZXRlLW5vdmlkYWRlcy1wYXJhLW9zLWRvbm9zLWRvLW5pbnRlbmRvLXN3aXRjaC9hbXAv?oc=5'}, {'author': 'Multiverso Notícias', 'title': "'Redfall' e expectativas frustradas: o que deu errado para o game? - Multiverso Notícias", 'url': 'https://news.google.com/rss/articles/CBMiWGh0dHBzOi8vbXVsdGl2ZXJzb25vdGljaWFzLmNvbS5ici9yZWRmYWxsLWUtYXMtZXhwZWN0YXRpdmFzLWZydXN0cmFkYXMtby1xdWUtZGV1LWVycmFkby_SAQA?oc=5'}, {'author': 'TudoCelular.com', 'title': 'Nitro Deck é novo controle Premium para Nintendo Switch; veja detalhes - TudoCelular.com', 'url': 'https://news.google.com/rss/articles/CBMiYmh0dHBzOi8vd3d3LnR1ZG9jZWx1bGFyLmNvbS90ZWNoL25vdGljaWFzL24yMDcyODgvbml0cm8tZGVjay1jb250cm9sZS1wcmVtaXVtLW5pbnRlbmRvLXN3aXRjaC5odG1s0gEA?oc=5'}, {'author': 'TecMundo', 'title': 'TOP 7 MELHORES WEBCAMS para trabalho, estudo EAD e streaming – 2023 - TecMundo', 'url': 'https://news.google.com/rss/articles/CCAiC256X0pycVFVUm93mAEB?oc=5'}]

        emails = ['destinatario1@example.com', 'destinatario2@example.com']
        sender_email = 'dadosclimaticos.uepb@gmail.com'
        sender_password = 'senha'
        template = """<tr>
          <td>
            <h1>{title}</h1>
            <h4>Autor:<strong> {author}</strong></h4>
            <p>Para ler mais, acesse: <a href="{url}">Ler mais</a></p>
          </td>
        </tr>"""

        yagmail_mock = MagicMock()
        yagmail_SMTP_mock = MagicMock(return_value=yagmail_mock)
        yagmail_mock.send = MagicMock()

        with unittest.mock.patch('meu_arquivo.yagmail.SMTP', yagmail_SMTP_mock):
            sendEmailNews(listNews, emails, sender_email, sender_password, template)

        yagmail_SMTP_mock.assert_called_once_with(sender_email, sender_password)
        yagmail_mock.send.assert_called_once_with(to=emails, subject='Newsletter Computing - UEPB', contents=unittest.mock.ANY)

if __name__ == '__main__':
    unittest.main()
