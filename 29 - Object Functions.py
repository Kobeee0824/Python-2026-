class Student:      
  def __init__(self, name, major, gpa, is_on_probation):
      self.name = name
      self.major = major
      self.gpa = gpa
      self.is_on_probation = is_on_probation

  #new code
  def on_honor_roll(self):  #new method - giving information about the class or modifying the information about the class
     if self.gpa >= 3.5:
        return True
     else: 
        return False

          

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Kiele", "Information Technology", 1.23, False)

print(f"{student1.name} {student1.major} {student1.gpa} {student1.is_on_probation}")

print(f"{student2.name} {student2.major} {student2.gpa} {student2.is_on_probation}")


print(student1.on_honor_roll())