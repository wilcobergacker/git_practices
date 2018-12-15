class Student:
  #method that adds all student info
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  #method that checks if grade is type Grade and if so adds it to student grades
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
#three instances of the Student class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
#method with a minimum passing and assigning of score
class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score
#extra method to print and give information
  def __repr__(self):
    return str(self.score)
#add 100 score to Pieter
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(55))

print(pieter.grades)
print(pieter.name)
