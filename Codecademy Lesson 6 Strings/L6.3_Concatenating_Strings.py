# You can also concatenate two existing strings together into a new string. Consider the following two strings.

fruit_prefix = "blue"
fruit_suffix = "berries"

favorite_fruit = fruit_prefix + fruit_suffix
print(favorite_fruit)
# => 'blueberries

first_name = "Julie"
last_name = "Blevins"

def account_generator(first, last):
  new = first_name[0:3] + last_name[0:3]
  return new

new_account = account_generator(first_name, last_name)
print(new_account)
