import click

class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.stocks = {}  # {stock_name: quantity}
        self.target_prices = {}  # {stock_name: target_price}

    def add_stock(self, stock_name, quantity):
        if stock_name in self.stocks:
            self.stocks[stock_name] += quantity
        else:
            self.stocks[stock_name] = quantity

    def set_target_price(self, stock_name, target_price):
        self.target_prices[stock_name] = target_price

    def buy_stock(self, seller, stock_name, quantity, transaction_amount, market):
        if stock_name in seller.stocks and stock_name in self.target_prices:
            if seller.target_prices[stock_name] <= self.target_prices[stock_name]:
                if seller.stocks[stock_name] >= quantity:
                    if self.balance >= transaction_amount:
                        self.balance -= transaction_amount
                        seller.balance += transaction_amount
                        seller.add_stock(stock_name, quantity)
                        seller.stocks[stock_name] -= quantity
                        market.record_transaction(self, seller, stock_name, quantity, transaction_amount)
                        click.echo(f"{self.username} bought {quantity} shares of {stock_name} from {seller.username}")
                    else:
                        click.echo("Insufficient balance to buy stock.")
                else:
                    click.echo(f"{seller.username} doesn't have enough {stock_name} to sell.")
            else:
                click.echo(f"{seller.username}'s target price for {stock_name} is higher than yours.")
        else:
            click.echo("Invalid stock or target price.")

    def __str__(self):
        return f"Username: {self.username}, Balance: ${self.balance}, Stocks: {self.stocks}"

class StockMarket:
    def __init__(self):
        self.transactions = []
        self.stock_prices = {}

    def record_transaction(self, buyer, seller, stock_name, quantity, amount):
        self.transactions.append({
            "buyer": buyer.username,
            "seller": seller.username,
            "stock_name": stock_name,
            "quantity": quantity,
            "amount": amount
        })

    def set_stock_price(self, stock_name, price):
        self.stock_prices[stock_name] = price

    def get_stock_price(self, stock_name):
        return self.stock_prices.get(stock_name, 0)

    def display_transactions(self):
        click.echo("=== Transaction History ===")
        for transaction in self.transactions:
            click.echo(f"Buyer: {transaction['buyer']}, Seller: {transaction['seller']}, "
                       f"Stock: {transaction['stock_name']}, Quantity: {transaction['quantity']}, "
                       f"Amount: ${transaction['amount']}")

class UserNotFoundException(Exception):
    pass

class MarketNotFoundException(Exception):
    pass

class MarketManager:
    users = {}
    def __init__(self):
        self.market = StockMarket()

    def find_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise UserNotFoundException(f"User '{username}' not found.")

    def get_market(self):
        return self.market

    def create_user(self, username, balance):
        user = User(username, balance)
        self.users[username] = user
        click.echo(f"User '{user.username}' with balance ${user.balance} created.")

    def add_stock(self, username, stock_name, quantity):
        user = self.find_user(username)
        user.add_stock(stock_name, quantity)
        click.echo(f"Added {quantity} shares of {stock_name} to {user.username}'s stocks.")

    def set_target_price(self, username, stock_name, target_price):
        user = self.find_user(username)
        user.set_target_price(stock_name, target_price)
        click.echo(f"Set target price for {stock_name} to ${target_price} for {user.username}.")

    def buy_stock(self, buyer, seller, stock_name, quantity, transaction_amount):
        buyer_user = self.find_user(buyer)
        seller_user = self.find_user(seller)
        market = self.get_market()
        buyer_user.buy_stock(seller_user, stock_name, quantity, transaction_amount, market)

    def display_transactions(self):
        market = self.get_market()
        market.display_transactions()

    def display_user(self, username):
        user = self.find_user(username)
        click.echo(user)

@click.group()
def mycommands():
    pass

# Menu
def main():
  value = click.prompt(
      'Select a command to run',
      type=click.Choice(list(mycommands.commands.keys()) + ['exit']))
  if value != 'exit': # if user enter a valid command
    mycommands.commands[value]() # run the command

@click.command()
@click.option("--username", prompt="Enter your username", help="The name of the user")
@click.option("--balance", prompt="Enter your balance", type=float, help="The balance of the user")
def create_user(username, balance):
    manager.create_user(username, balance)
    main() # call main again 

@click.command()
@click.option("--username", prompt="Enter your username", help="The name of the user")
@click.option("--stock_name", prompt="Enter the stock name", help="The name of the stock")
@click.option("--quantity", prompt="Enter the quantity", type=int, help="The quantity of stock to add")
def add_stock(username, stock_name, quantity):
    manager.add_stock(username, stock_name, quantity)
    main() # call main again

@click.command()
@click.option("--username", prompt="Enter your username", help="The name of the user")
@click.option("--stock_name", prompt="Enter the stock name", help="The name of the stock")
@click.option("--target_price", prompt="Enter the target price", type=float, help="The target price for the stock")
def set_target_price(username, stock_name, target_price):
    manager.set_target_price(username, stock_name, target_price)
    main() # call main again
  

@click.command()
@click.option("--buyer", prompt="Enter the buyer's username", help="The name of the buyer")
@click.option("--seller", prompt="Enter the seller's username", help="The name of the seller")
@click.option("--stock_name", prompt="Enter the stock name", help="The name of the stock")
@click.option("--quantity", prompt="Enter the quantity", type=int, help="The quantity of stock to buy")
@click.option("--transaction_amount", prompt="Enter the transaction amount", type=float, help="The transaction amount")
def buy_stock(buyer, seller, stock_name, quantity, transaction_amount):
    manager.buy_stock(buyer, seller, stock_name, quantity, transaction_amount)
    main() # call main again


@click.command()
def display_transactions():
    manager.display_transactions()
    main() # call main again

@click.command()
@click.option("--username", prompt="Enter your username", help="The name of the user")
def display_user(username):
    manager.display_user(username)
    main() # call main again

mycommands.add_command(create_user)
mycommands.add_command(add_stock)
mycommands.add_command(set_target_price)
mycommands.add_command(buy_stock)
mycommands.add_command(display_transactions)
mycommands.add_command(display_user)

# RUN ONLY python3 main.py
# DO NOT USE ANY COMMAND WHILE STARTING THE PROGRAM !!!!
if __name__ == "__main__":
    manager = MarketManager()
    main() # Add main function to start the menu
