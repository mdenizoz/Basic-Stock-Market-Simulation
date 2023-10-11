# tests/test_advanced.py

import unittest
from sample.core import User, StockMarket, MarketManager

class TestAdvancedFunctionality(unittest.TestCase):
    def setUp(self):
        # Initialize test data or setup for your tests, if needed
        self.market_manager = MarketManager()

    def test_buy_stock(self):
        self.market_manager.create_user("buyer", 3000)
        self.market_manager.create_user("seller", 500)
        self.market_manager.add_stock("seller", "AAPL", 5)
        self.market
