
from unittest.mock import patch, MagicMock,Mock
import unittest
from src.controller import controller
from src.repo import repository

base_input = ["AZAZAZAZAZ_8", "абвгдежН7_", "абвгдежН7_"]
class Test(unittest.TestCase):
    @patch("builtins.input", side_effect=[base_input,base_input])
    def test_add_user(self,mock_input):
        c = controller()
        value,err = c.add()
        self.assertTrue(value)

    @patch("builtins.input", side_effect=[base_input,base_input])
    def test_get_user(self,mock_input):
        c = controller()
        value, err = c.add()
        value,err = c.get()
        self.assertIsNotNone(value)

    @patch("builtins.input", side_effect=[base_input,base_input])
    def test_delete_user(self,mock_input):
        c = controller()
        value, err = c.add()
        value,err = c.delete()
        self.assertTrue(value,"не удалилось")


    def set_bd(self):
        self.repo = repository()
        self.assertIsNotNone(self.repo.connection,"Не создается соединение")


    def test_bd_table(self):
        self.repo = repository()
        self.repo.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
        )
        row = self.repo.cursor.fetchone()
        self.assertIsNotNone(row, "Таблица users не создана")


if __name__ == '__main__':
    unittest.main()
