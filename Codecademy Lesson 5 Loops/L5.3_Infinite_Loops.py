students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for students in students_period_A:
  students_period_B.append(students) # if you change students_period_B to students_period_A, it will cause an infinite loop
  print(students)

# temp variable represents elemenets in the lists
