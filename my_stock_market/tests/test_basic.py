# tests/test_basic.py

import unittest
from sample.core import User, StockMarket, MarketManager

class TestBasicFunctionality(unittest.TestCase):
    def setUp(self):
        # Initialize test data or setup for your tests, if needed
        self.market_manager = MarketManager()

    def test_create_user(self):
        self.market_manager.create_user("user1", 1000)
        user = self.market_manager.find_user("user1")
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.balance, 1000)

    def test_add_stock(self):
        self.market_manager.create_user("user2", 1500)
        self.market_manager.add_stock("user2", "AAPL", 10)
        user = self.market_manager.find_user("user2")
        self.assertEqual(user.stocks.get("AAPL"), 10)

    def test_set_target_price(self):
        self.market_manager.create_user("user3", 2000)
        self.market_manager.set_target_price("user3", "GOOGL", 1500)
        user = self.market_manager.find_user("user3")
        self.assertEqual(user.target_prices.get("GOOGL"), 1500)

if __name__ == '__main__':
    unittest.main()
