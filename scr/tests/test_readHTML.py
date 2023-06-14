import unittest
from scr.functions.template.readHTML import read_html_file

class TestReadHTMLFile(unittest.TestCase):

    def test_read_html_file(self):
        file_path = '../functions/template/template.html'
        expected_content = """<tr>
  <td>
    <h1>{title}</h1>
    <h4>Autor:<strong> {author}</strong></h4>
    <p>Para ler mais, acesse: <a href="{url}">Ler mais</a></p>
  </td>
</tr>"""

        content = read_html_file(file_path)

        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()
