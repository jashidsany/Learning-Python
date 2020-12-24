# A string is a list of characters.
# A character can be selected from a string using its index string_name[index]. These indices start at 0.
# A ‘slice’ can be selected from a string. These can be between two indices or can be open-ended, selecting all of the string from a point.
# Strings can be concatenated to make larger strings.
# len() can be used to determine the number of characters in a string.
# Strings can be iterated through using for loops.
# Iterating through strings opens up a huge potential for applications, especially when combined with conditional statements.

# This function takes the first 3 letters of the first and first 4 of the last and concatenates it
def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4]
  return username

print(username_generator("Abe", "Simpson"))
print(username_generator("Emma", "Jay"))

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
      # for elements in the range of 0 and the length of the list
        password += user_name[i-1]
      # add those elements to the string password by shifting it all to the right
    return password

print(password_generator("Abesimp"))
