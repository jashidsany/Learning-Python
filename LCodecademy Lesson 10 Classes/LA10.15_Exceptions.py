#  An Exception is a class that inherits from Python’s Exception class.
# We can validate this ourselves using the issubclass() function. issubclass() is a Python built-in function that takes two parameters. issubclass() returns True if the first argument is a subclass of the second argument. It returns False if the first class is not a subclass of the second. issubclass() raises a TypeError if either argument passed in is not a class.

# Define your exception up here:
class OutOfStock(Exception):
  pass

# Update the class below to raise OutOfStock
class CandleShop(OutOfStock):
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock

  def buy(self, color):
    self.stock[color] = self.stock[color] - 1
    if self.stock[color] < 1:
      raise OutOfStock

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')
