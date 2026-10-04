
from unittest.mock import patch, MagicMock,Mock
import unittest
from src.controller import controller
from src.repo import repository
from src.user_input import user_input

base_input = ["AZAZAZAZAZ_8", "абвгдежН7_", "абвгдежН7_"]

class test_controller(unittest.TestCase):
    @patch("builtins.input", side_effect=base_input)
    def test_add_user(self,mock_input):
        c = controller()
        value,err = c.add()
        self.assertTrue(value)

    @patch("builtins.input", side_effect=base_input*2)
    def test_get_user(self,mock_input):
        c = controller()
        value, err = c.add()
        value,err = c.get()
        self.assertIsNotNone(value)

    @patch("builtins.input", side_effect=base_input *2)
    def test_delete_user(self,mock_input):
        c = controller()
        value, err = c.add()
        value,err = c.delete()
        self.assertTrue(value,"не удалилось")


class test_Repository(unittest.TestCase):
    def test_set_bd(self):
        self.repo = repository()
        self.assertIsNotNone(self.repo.connection, "Не создается соединение")

    def test_bd_table(self):
        self.repo = repository()
        self.repo.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
        )
        row = self.repo.cursor.fetchone()
        self.assertIsNotNone(row, "Таблица users не создана")

class test_user_input(unittest.TestCase):
    @patch("builtins.input", side_effect=base_input)
    def test_input(self,mock_input):
        self.user_input = user_input()
        l,p,p2 = self.user_input.input()
        self.assertEqual(l,base_input[0])
        self.assertEqual(p,base_input[1])
        self.assertEqual(p2,base_input[2])
if __name__ == '__main__':
    unittest.main()
