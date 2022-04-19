class Student(object):
	def __init__(self,name,age,gender,level,grades=None):
		self.name = name
		self.age = age
		self.gender = gender
		self.level = level
		self.grades = grades or {}
	def setGrade(self,course,grade):
		self.grades[course] = grade

	def setGrade(self,course):
		return self.grades[course]

	def getGPA(self):
		return sum(self.grades.values())/len(self.grade)

c1 = Student("Gautham", 13, "male", 8, {"math":4.5})
c2 = Student("Cynna", 13, "female", 8, {"math":3.5})

print(c1.name)
print(c2.gender)