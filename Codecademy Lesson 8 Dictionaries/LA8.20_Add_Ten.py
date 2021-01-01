# Write your add_ten function here:
def add_ten(my_dictionary):
  for keys in my_dictionary.keys():
    # iterates through the keys in the dictionary
    my_dictionary[keys] += 10
    # adds 10 to the value of the keys that are being looped through
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}
