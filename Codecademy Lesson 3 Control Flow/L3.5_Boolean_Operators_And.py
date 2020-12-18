statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)

def graduation_reqs(gpa, credits):
  if gpa >= 2.0 and credits >= 120:
    return "You meet the requirements to graduate!"
