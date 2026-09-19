import unittest
from datetime import datetime, timedelta
from src.Delivery import calculate_delivery_cost

invalidResponse = -1,"0000-00-00"
class TestDeliveryCost(unittest.TestCase):
    def test_invalid_package_type(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="invalid", is_express=False)
        respons = (cost, date)
        invalidResponse = -1, "0000-00-00"
        self.assertEqual(invalidResponse,respons)

    def test_invalid_package_weight(self):
        cost, date = calculate_delivery_cost(weight=100.0, distance=100,
                                             package_type="обычный", is_express=False)
        respons = (cost, date)
        invalidResponse = -1, "0000-00-00"
        self.assertEqual(invalidResponse, respons)

    def test_invalid_package_distance(self):
        cost, date = calculate_delivery_cost(weight=10.0, distance=100000,
                                             package_type="обычный", is_express=False)
        respons = (cost, date)
        invalidResponse = -1, "0000-00-00"
        self.assertEqual(invalidResponse, respons)
    def test_normal_package_cost(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="обычный", is_express=False)
        respons = (cost, date)
        invalidResponse = -1, "0000-00-00"
        self.assertNotEqual(respons, invalidResponse)
    def test_package_cost(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="обычный", is_express=False)

        trueCost = 200+(100 * 5)

        respons = (cost, date)
        self.assertEqual(trueCost, cost)
    def test_delivery_data(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="обычный", is_express=False)
        respons = [cost, date]
        invalidResponse = -1, "0000-00-00"
        day = max(1,100//500)
        day = timedelta(days = day) + datetime.now()
        day = day.strftime("%Y-%m-%d")
        self.assertEqual(day,date)
    def test_express_package_cost(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="обычный", is_express=True)

        trueCost = (200 + (100 * 5))
        trueCost = trueCost*0.5

        respons = (cost, date)
        self.assertEqual(trueCost, cost)

    def test_express_delivery_package_data_(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="обычный", is_express=True)
        respons = [cost, date]
        invalidResponse = -1, "0000-00-00"
        day = max(1,100//500)
        day = day//2
        day = timedelta(days = day) + datetime.now()
        day = day.strftime("%Y-%m-%d")
        self.assertEqual(day,date)
    def test_express_delivery_package_type_fragile_cost(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="хрупкий", is_express=True)
        respons = [cost, date]
        trueCost = (200 + (100 * 5))
        trueCost = trueCost+300
        trueCost = trueCost * 0.5
        self.assertEqual(trueCost, cost)

    def test_express_delivery_package_type_danger_cost(self):
        cost, date = calculate_delivery_cost(weight=2.0, distance=100,
                                             package_type="опасный", is_express=True)
        respons = [cost, date]
        trueCost = (200 + (100 * 5))
        trueCost = trueCost+1000
        trueCost = trueCost * 0.5
        self.assertEqual(trueCost, cost)
if __name__ == '__main__':
    unittest.main()
