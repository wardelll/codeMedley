# Python basics
print("Hello, World!")
if(5 > 2):
 print("Five is greater than two")
 
# Variables 
x = 5
y = "Hello, Again!"

print(x)
print(y)


# Cast int to str and float
x = str(3)
y = float(3)

print(type(x))
print(type(y))


# Assign multiple variables in one line
x, y, z = "Ornge", "Apple", "Banna"
print(x)
print(y)
print(z)

# Assign one value to multiple variables
x = y = z = "Apple"
print(x)
print(y)
print(z)

# Unpack a list/collection
fruits = ["apple", "banna", "ornge"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Print multiple values in a single function
print(x, y, z)

# Function
def myfunc():
 	print("My fruit list: " + x, y, z)
 	
myfunc()

# Use the random module to generate random numbers
import random
print(random.randrange(1, 10))

