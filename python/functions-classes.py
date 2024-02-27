# create
def myfunction():
	print("Hello world!")
	
# call
myfunction()

# param
def myfunction(username):
	print("Hello " + username + "!")
	
myfunction("Bob")
myfunction("Kim")
	
# arbitrary number of arguments
def myfunction(*people):
	print("Hello " + people[1] + "!")
	
myfunction("Kim", "Bob")

# arbitrary number of keyword arguments
def myfunction(**person):
	print("Hello " + person["first"] + "!")
	
myfunction(first = "Kim", second = "Bob")

# Lambda
x = lambda a : a + 10
print(x(5))

# Create a class
class Person: 
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
p1 = Person("Sarah", 35)

print(p1.name)
print(p1.age)

# represent class as string 
class Person: 
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def __str__(self):
		return f"{self.name}({self.age})"
		
p1 = Person("Sarah", 35)
print(p1)


# child class with inherited __init__() function
class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)
		
# child class with all inherited functions and properties 
class Student(Person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
