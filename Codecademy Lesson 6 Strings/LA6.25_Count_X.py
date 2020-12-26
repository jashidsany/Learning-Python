# Write your count_char_x function here:
def count_char_x(word, character = "x"):
  count = 0
  # a counter
  for letter in word:
    # for each letter in the word
    if character in letter:
      # if the character matches any of the letters in the word
      count += 1
      # add to the count
  return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
print(count_char_x("apple", "p"))
# should print 2
