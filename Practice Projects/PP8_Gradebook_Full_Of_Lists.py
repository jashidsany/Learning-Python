last_semester_gradebook = [(80, "politics"), (96, "latin"), (97, "dance"), (65, "architecture")]

subjects = ["physics", "calculus", "poetry", "history"]
subjects.append("computer science")
print(subjects)

grades = [98, 97, 85, 88]
grades.append(100)
print(grades)

print("\n")

gradebook = list(zip(grades, subjects))
gradebook.append((93, "visual arts"))
print(list(gradebook))

print("\n")

full_gradebook = last_semester_gradebook + gradebook
print(list(full_gradebook))
