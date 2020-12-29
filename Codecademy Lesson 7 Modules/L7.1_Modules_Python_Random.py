# random.choice() which takes a list as an argument and returns a number from the list
# random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1, 100) for i in range(101)]
# List comprhension = [what_will_replace_i for i in some_list_or_range]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
