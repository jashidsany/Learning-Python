# Write your add_exclamation function here:
def add_exclamation(word):
  while(len(word) < 20):
    # loops through the length of word
    word += "!"
    # adds "!" to it until it gets to 20 characters
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
