import unittest
from src.database import DatabaseRepository as DbRepository
from src.controller import controller as c, controller
from tests.test_parser import parser

html_file = ""
with open('page.html', encoding='utf-8') as f:
    html_file = f.read()

result_pars = parser.parse_html(html_file)
database_url = 'database.db'
class MyTestCase(unittest.TestCase):
    def test_add_comment_error_ID(self):
        controller = c(DbRepository(database_url))
        value,err =controller.parse_html(html_file)
        value2, err2 = controller.parse_html(html_file)
        self.assertEqual(value2,False)
    def test_add_comment_success(self):
        controller = c(DbRepository(':memory:'))
        value, err = controller.parse_html(html_file)
        self.assertEqual(value, True)
    def test_get_by_id_wrong_id(self):
        db = DbRepository(database_url)
        valid, err = db.get_by_id(1)
        self.assertEqual(valid, None)
    def test_get_by_id_success(self):
        db = DbRepository(database_url)
        valid, err = db.get_by_id(result_pars[0][0])
        self.assertIsNotNone(valid)
    def test_get_by_name_wrong_name(self):
        db = DbRepository(database_url)
        valid, err = db.get_by_name("egorka")
        self.assertIsNone(valid)
    def test_get_by_name_success(self):
        db = DbRepository(database_url)
        name = result_pars[0][1]
        valid, err = db.get_by_name(name)
        self.assertIsNotNone(valid)
    def test_update_comment_wrong(self):
        db = DbRepository(database_url)
        result, err = db.update(3,"ne")
        self.assertEqual(result, False)
    def test_update_comment_success(self):
        db = DbRepository(database_url)
        result, err = db.update(result_pars[0][0],"ne")
        self.assertEqual(result, True)

if __name__ == '__main__':
    controller = c(DbRepository(database_url))
    value, err = controller.parse_html(html_file)
    unittest.main()
