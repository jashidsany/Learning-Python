# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  # creates 2 variables for key and value
  for key, value in my_dictionary.items():
    # loops through the items in my_dictionary
    if value > largest_value:
      # if the value in the dictionary is larger
      largest_value = value
      # largest_value becomes that value
      largest_key = key
      # largest_key becomes that key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
