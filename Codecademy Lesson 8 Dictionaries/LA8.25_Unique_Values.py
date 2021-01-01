# Write your unique_values function here:
def unique_values(my_dictionary):
 seen_values = []
 # creates a new list
 for value in my_dictionary.values():
   # loops through the values in my_dictionary
    if value not in seen_values:
      # if the value is not in the list
      seen_values.append(value)
      # append it to the list
 return len(seen_values)
 # returns the length of the list seen_values

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
