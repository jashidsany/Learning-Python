# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  # create a variable splits that equals to the word.split(string parameter)
  return(len(splits)-1)
  # return the length of splits

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
