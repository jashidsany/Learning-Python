# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  sum = 0
  for keys, values in my_dictionary.items():
    # iterates through the items in my_dictionary
    if keys % 2 == 0:
      # if the keys are even
      sum += values
      # add the values to the sum
  return sum

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6
