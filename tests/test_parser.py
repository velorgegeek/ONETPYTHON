import unittest
from src.parser import ForumParser as parser
html_file = ""
with open('page.html', encoding='utf-8') as f:
    html_file = f.read()

invalid_url = 'link'
parser = parser()
class MyTestCase(unittest.TestCase):
    def test_parser_valid(self):
          result = parser.parse_html(html_file)
          self.assertNotEqual(result, [])
    def test_parser_invalid(self):
        result = parser.parse_html(invalid_url)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
