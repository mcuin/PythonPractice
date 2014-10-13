#!/urs/bin/python

class Employee:
	empCount = 0
	
	def __init__ (self, name, salary):
		'Common base class for all employees.'
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displyCount(self):
		print "Total employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name: ", self.name, ", Salary: ", self.salary

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Number of employees %d" % Employee.empCount

print "Employee.__doc__: ", Employee.__doc__
print "Employee.__name__: ", Employee.__name__
print "Employee.__module__: ", Employee.__module__
print "Employee.__bases__: ", Employee.__bases__
print "Employee.__dict__: ", Employee.__dict__

class Point:
	def __init(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt1

print id(pt1), id(pt2), id(pt3)

del pt1
del pt2
del pt3

class Parent:
	parentAttr = 100
	
	def __init__(self):
		print "Calling parent constructor"

	def parentMethod(self):
		print "Calling parent method"

	def setAttr(self, attr):
		Parent.parentArrt = attr

	def getAttr(self):
		print "Parent attribute: ", Parent.parentAttr

	def myMethod(self):
		print "Calling parent method"

class Child(Parent):
	
	def __init__(self):
		print "Calling child constructor"

	def childMethod(self):
		print "Calling child method"

	def myMethod(self):
		print "Calling child method"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()

class Vector:
	
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d, %d)' % (self.a, self.b)

	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)

print v1 + v2

class JustCounter:
	__secretCount = 0
	
	def count(self):
		self.__secretCount += 1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.__secrentCount	
