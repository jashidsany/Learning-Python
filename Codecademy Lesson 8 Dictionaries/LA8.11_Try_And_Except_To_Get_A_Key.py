# We saw that we can avoid KeyErrors by checking if a key is in a dictionary first. Another method we could use is a try/except:
# key_to_check = "Landmark 81"
# try:
#  print(building_heights[key_to_check])
# except KeyError:
#  print("That key doesn't exist!")
# When we try to access a key that doesn’t exist, the program will go into the except block and print "That key doesn't exist!".

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}

try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")
