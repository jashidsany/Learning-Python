# Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:
# names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# heights = [61, 70, 67, 64]
# Python allows you to create a dictionary using a list comprehension, with this syntax:
# students = {key:value for key, value in zip(names, heights)}
# students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
# Remember that zip() combines two lists into a zipped list of pairs. This list comprehension:
# Takes a pair from the zipped list of pairs from names and heights
# Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
# Creates a key : value item in the students dictionary
# Repeats steps 1-3 for the entire list of pairs

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drinks:caffeine for drinks, caffeine in zipped_drinks}
print(drinks_to_caffeine)
