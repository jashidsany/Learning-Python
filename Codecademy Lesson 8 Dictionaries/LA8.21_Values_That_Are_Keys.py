# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  count = []
  # a new list
  for value in my_dictionary.values():
    # iterates through the values in the dictionary
    if value in my_dictionary.keys():
      # if the value is the same as the keys append it to count
      count.append(value)
  return count

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
