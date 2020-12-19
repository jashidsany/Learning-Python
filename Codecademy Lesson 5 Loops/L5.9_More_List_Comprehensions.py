# This list comprehension:
# Takes a string in usernames
# Assigns that string to a variable called user
# Adds “ please follow me!” to user
# Appends that concatenation to the new list called messages
# Repeats steps 1-4 for all of the strings in usernames

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [(degree * 9/5) + 32 for degree in celsius]
# each degree is converted to fahrenheit from celsius in the celsius
print(fahrenheit)
