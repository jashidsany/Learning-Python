# This list comprehension:
# usernames = [word for word in words if word[0] == '@']
# Takes an element in words
# Assigns that element to a variable called word
# Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
# Repeats steps 1-3 for all of the strings in words
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
# temp variable is created called height which has the elements of heights
# so for every height in heights that are less greater than 161 store it into can_ride_coaster 
print(can_ride_coaster)
