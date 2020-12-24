# You can count how many specific letters there are in a string.

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

# This function iterates through the word and checks if it has a char = to letter
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

letter_check("strawberry", 'a')
)
