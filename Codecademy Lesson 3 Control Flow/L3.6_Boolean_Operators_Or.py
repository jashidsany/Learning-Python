statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
print(statement_one)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
print(statement_two)

def graduation_mailer(gpa, credits):
  if gpa >= 2.0 or credits >= 120:
    return True
