# We can iterate through a string using in
# The syntax for in is: letter in word

# Here, letter in word is a boolean expression that is True if the string letter is in the string word. Here are some examples:
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

# In fact, this method is more powerful than the function you wrote in the last exercise because it not only works with letters, but with entire strings as well.
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False

# This function checks if the little string is in the big string
def contains(big_string, little_string):
    if little_string in big_string:
      return True
    else:
      return False

print(contains('watermelon', 'melon'))
print(contains('watermelon', 'berry'))

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    # iterate through the letters in string_one
    if (letter in string_two) and not (letter in common):
      # if letter is in string_two and not in the list of common append it
      common.append(letter)
  return common

print(common_letters('manhattan', 'san francisco'))
