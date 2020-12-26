letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  uniques = 0
  # uniques is a counter
  for letter in letters:
    # iterate each letter in the string letters
    if letter in word:
      # if a letter appears in the string used in the function's parameter
      uniques += 1
      # add one to the counter
  return uniques
    # return counter

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("Count"))
# should print 5
