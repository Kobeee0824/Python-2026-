#You can create your own data type in classes and objects
#You can define your own data type

#gamit ang student na as your class, pwede mo assign yung iba't ibang values or datatypes such as text, numbers, and boolean

class Student:       #ito yung may iba't ibang data type sa baba, values lang yan na pinasa (parameters)
  def __init__(self, name, major, gpa, is_on_probation):
      self.name = name
      self.major = major
      self.gpa = gpa
      self.is_on_probation = is_on_probation
#yung mga self.name, self.major, etc, mga attributes sila ng object

          #filename       #classname

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Kiele", "Information Technology", 1.23, False)

print(f"{student1.name} {student1.major} {student1.gpa} {student1.is_on_probation}")

print(f"{student2.name} {student2.major} {student2.gpa} {student2.is_on_probation}")
