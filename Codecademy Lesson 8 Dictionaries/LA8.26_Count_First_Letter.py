# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names:
    # loops through names
    first_letter = key[0]
    # the first letter is equal to the value of the first index
    if first_letter not in letters:
      # if first_letter is not in the dictionary letters
      letters[first_letter] = 0
      # it is given a value of 0
    letters[first_letter] += len(names[key])
    # adds the length of the keys in names to the variable first_letters
  return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
