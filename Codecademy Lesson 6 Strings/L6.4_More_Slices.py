favorite_fruit = "blueberry"
length = len(favorite_fruit)
# len takes the number of char in the string "blueberry"
print(length)
# => 9

fruit_sentence = "I love blueberries"
print(len(fruit_sentence))
# spaces count as char
# => 18

# last_char = favorite_fruit[len(favorite_fruit)]
# print(last_char)
# => IndexError
# this will create an index error because the string only has 8 indicies
# len(favorite_fruit) returns a index of 9

last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char)
# => 'y'
# you have to use the -1 index to access the final index

length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)
# => 'erry'
# you can use -4 to access the last 4 indicies of the string

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)
print(temp_password)
