# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  # create a variable reverse and set equal to an empty string
  for i in range(len(word)-1, -1, -1):
    # for in the range of the length of word, reverse it
    reverse += word[i]
    # add that i to the empty string
  return reverse

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
