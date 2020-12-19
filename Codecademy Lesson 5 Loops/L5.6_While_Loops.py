all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6: # while the length of students_in_poetry is less than 6 run the following block of code
  student = all_students.pop()
  students_in_poetry.append(student)

print(students_in_poetry)
