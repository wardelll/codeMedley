# Multiline string
a = """One two three
A B C
red blue yellow"""
print(a)

# String as array
print(a[1])

# For loop
for x in "python":
 print(x)
 
# String length
print(len(a))

# Substring check
print("red" in a)
print("green" not in a)

# Array slice
# omiting the starting index will start from first index
# omiting the end index will go to the end
print(a[0:7])

# Use negative indexes to start from the end 
print(a[-6:])

# Transform case
a = " Hello, World! "
print(a.upper())
print(a.lower())

# Remove leading and trailing whitespace
print(a.strip())

# Replace String
print(a.replace("H", "J"))

# Split String
print(a.split(","))

# Place number into string
amount = 10
cost = 15
text = "{} thingamajigs for {} dolars"
print(text.format(amount, cost))

# Specify indexes
amount = 10
cost = 15
text = "{1} thingamajigs for {0} dolars"
print(text.format(amount, cost))
