# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    # iterates through words
    if word not in freqs:
      # if the word is not in the dictionary freqs
      freqs[word] = 0
      # the value becomes 0
    freqs[word] += 1
       # add 1 everytime the word pops up in the loop
  return freqs

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
