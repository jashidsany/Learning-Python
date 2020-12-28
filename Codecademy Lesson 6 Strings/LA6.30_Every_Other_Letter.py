# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  # create a variable and set it equal to empty string
  for i in range(0, len(word), 2):
    # for i in the range of 0 to the length of word, skipping 2
    every_other += word[i]
    # add it to the empty string
  return every_other

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 
