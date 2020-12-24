# We can iterate through strings and use loops to print out each char in a string!

def print_each_letter(word):
  for letter in word:
    print(letter)

print_each_letter("alpaca")

# Uses a counter to count how many letters in a word
def get_length(string):
  count = 0
  for rings in string:
    count += 1
  return count

print(get_length("twentyone"))
