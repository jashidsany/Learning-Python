class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self, grade):
    if type(grade) == Grade: # no () when using classes here
      self.grades.append(grade)

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

pieter.add_grade(Grade(100)) # to use the method just use the name and the class name and add the score you want
