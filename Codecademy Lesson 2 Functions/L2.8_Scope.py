'''
def create_special_string(special_item):
return "Our special is " + special_item + "."
print("I don't like " + special_item)

If we try to run this code, we will get a NameError, telling us that 'special_item' is not defined.
The variable special_item has only been defined inside the space of a function, so it does not exist outside the function.
We call the part of a program where special_item can be accessed its scope.
The scope of special_item is only the create_special_string function.
'''

current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)

print(calculate_age(1970))

# current_year can be used globablly if defined before the function. 
