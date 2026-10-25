import unittest
from src.main import do as d

class MyTestCase(unittest.TestCase):
    def test_x_equal_0(self):
        self.assertRaises(d(0), ValueError)
    def test_x_bigger_then_100(self):
        val = d(1005)
        self.assertEqual(val, 1000)


    def test_x_equal_5_point_5(self):
        # x>0 & x<100.7
        val =  d(5.5)
        self.assertEqual(val, 5)
    def test_x_equal_minus_20(self):
        # x ∈ [-30.4; 0)
        val = d(-20)
        self.assertEqual(val, -25)

    def test_x_equal_minus_100(self):
        # x ∈ [-30.4; 0)
        val = d(-100)
        self.assertEqual(val, 2000)

    def test_return_value(self ):

        self.assertIsNotNone(d(5))
    def test_return_value_exception(self):
        try:
            d(5)
        except ValueError:
            self.fail("ValueError not throw in this case")
if __name__ == '__main__':
    unittest.main()
