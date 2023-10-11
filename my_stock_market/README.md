# Stock Trading Simulator

Welcome to the Stock Trading Simulator! This Python project allows users to simulate buying and selling stocks on a virtual stock market. Users can create accounts, set target prices for stocks, and engage in stock trading with other users.

## Table of Contents

- [Usage](#usage)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Classes](#classes)
- [Contributing](#contributing)
- [License](#license)

## Usage

To use the Stock Trading Simulator, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the program using `python live_menu.py`.

The program provides a menu-driven interface for creating user accounts, setting target prices, buying and selling stocks, and displaying transaction history.

## Installation

To run the Stock Trading Simulator, you need Python installed on your system. You can install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```
## File Structure

The project's file structure is organized as follows:

- `live_menu.py`: The main Python script that implements the stock trading simulator.
- `sample/`: The directory containing core project code.
  - `core.py`: Contains the core classes and logic for the simulator.
  - `helpers.py`: Contains helper functions and utilities, if needed.
- `docs/`: Documentation files for the project.
- `tests/`: Test files to test the project's functionality.

## Classes

### User

- `__init__(self, username, balance)`: Initializes a user with a username and initial balance.
- `add_stock(self, stock_name, quantity)`: Adds stocks to the user's portfolio.
- `set_target_price(self, stock_name, target_price)`: Sets a target price for a specific stock.
- `buy_stock(self, seller, stock_name, quantity, transaction_amount, market)`: Allows a user to buy stocks from another user on the market.
- `__str__(self)`: Returns a string representation of the user's information.

### StockMarket

- `__init__(self)`: Initializes the stock market with empty transaction history and stock prices.
- `record_transaction(self, buyer, seller, stock_name, quantity, amount)`: Records a transaction in the market.
- `set_stock_price(self, stock_name, price)`: Sets the price of a specific stock.
- `get_stock_price(self, stock_name)`: Retrieves the price of a specific stock.
- `display_transactions(self)`: Displays the transaction history of the market.

### MarketManager

- `__init__(self)`: Initializes the market manager, managing user accounts and the stock market.
- `find_user(self, username)`: Finds a user by their username.
- `get_market(self)`: Retrieves the stock market instance.
- `create_user(self, username, balance)`: Creates a new user account.
- `add_stock(self, username, stock_name, quantity)`: Adds stocks to a user's portfolio.
- `set_target_price(self, username, stock_name, target_price)`: Sets a target price for a stock.
- `buy_stock(self, buyer, seller, stock_name, quantity, transaction_amount)`: Facilitates stock buying between users.
- `display_transactions(self)`: Displays the transaction history.
- `display_user(self, username)`: Displays user information.

### Contributing

Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request. Make sure to follow the project's code of conduct.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using the Stock Trading Simulator! Happy trading! 📈💰

