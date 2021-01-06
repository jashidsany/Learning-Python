# Python doesn’t stop at allowing us to accept unlimited positional parameters, it gives us the power to define functions with unlimited keyword parameters too. The syntax is very similar, but uses two asterisks (**) instead of one. Instead of args, we call this kwargs — as a shorthand for keyword arguments.
# Since we’re not sure whether a keyword argument will exist, it’s probably best to use the dictionary’s .get() method to safely retrieve the keyword argument. Do you remember what .get() returns if the key is not in the dictionary? It’s None!

# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(
	name="Tim",
  feeling="10/10",
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  Baseball='3',
  Shirt='14',
  Guitar='70')
