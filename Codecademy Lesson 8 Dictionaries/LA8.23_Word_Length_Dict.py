# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    # iterates through words
    word_lengths[word] = len(word)
    # word becomes the key and the length of that word is the value
    # stores it all in the dictionary word_lengths
  return word_lengths

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
