first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
print(first_names)

age = []
print(age)

age.append(42)
print(age)

all_ages = [32, 41, 29] + age
print(all_ages)

name_and_age = zip(first_names, all_ages)
print(list(name_and_age))

ids = range(0, 4)
print(list(ids))
