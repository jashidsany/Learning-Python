# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split(" ")
  # creates a variable words that stores the words split in the string sentence
  for word in words:
    # iterates through the words
    if len(word) < x:
      # if the length of the word is less than the integer x
      return False
  return True

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
