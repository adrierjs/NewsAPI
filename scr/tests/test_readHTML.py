import unittest
from scr.functions.template.readHTML import read_html_file

class TestReadHTMLFile(unittest.TestCase):

    def test_read_html_file(self):
        file_path = 'scr/functions/template/template.html'
        expected_content = """<tr>
  <td>
    <h1>{title}</h1>
    <p>{description}</p>
    <p><strong>Fonte: </strong>{source_name}</p>
    <p>Para ler mais, <strong>acesse: </strong> <a href="{url}">Ler mais</a></p>
    <p><strong>Data de publição:</strong>{publishedAt}</p>
  </td>
</tr>"""

        content = read_html_file(file_path)

        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()
