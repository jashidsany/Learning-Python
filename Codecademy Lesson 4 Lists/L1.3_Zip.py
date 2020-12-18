# If we wanted to create a list of lists that paired each name with a height, we could use the command zip.

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = (list(names_and_dogs_names))
print(list_of_names_and_dogs_names)
