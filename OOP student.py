#SEAT No. EB20102140
#NAME:UMAIR IQBAL
#BSCS(A) Evening

class Students():
  def __init__(self,name,age,grade):
    self.name = name
    self.age = age
    self.grade = grade
  def get_name(self):
   return self.name
  def get_age(self):
   return self.age
  def get_grade(self):
    return self.grade
  def update_grade(self,update):
    self.grade = update
    return

std1 = Students('umair',20,75)

std2 = Students('daniyal',18,90)

std3 = Students('tariq',20,89)

std4 = Students('anees',21,90)

class courses():
  def __init__(self,course,max_stud):
    self.course = course
    self.students = []
    self.max_stud = max_stud
  def add_stud(self,student):
    if len(self.students) < (self.max_stud):
      self.students.append(student)
      print(student.name,student.grade)
    else:
      print("Max students are already there")
  def get_grades(self):
    all_grades = []
    for i in range(len(self.students)):
      stud = self.students[i]
      all_grades.append(stud.grade)
    return all_grades
  def avg_grade(self):
    avg_grades = (sum(course.get_grades())) / self.max_stud
    return avg_grades

course = courses('ICS',3)
course.add_stud(std1)
course.add_stud(std2)
course.add_stud(std3)
course.add_stud(std4)

print(std1.name,std2.name,std3.name)
print('grades',course.get_grades())

print(course.course,'average of grades is',course.avg_grade())
