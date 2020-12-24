# Strings are immutable and cannont be changed. You create new strings through the process of concatenating and slicing.

first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"
# this will produce an error

fixed_first_name = "R" + first_name[1:3] # it's 1:3 because it ends 2
print(fixed_first_name)
