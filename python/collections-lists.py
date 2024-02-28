# Lists
mylist = ["apple", "banana", "orange", "strawberry"]
print(mylist)

# Change list Item
mylist[1] = "cherry"
print(mylist)

# Change a range of items (up to but not including the 3rd index)
# if more items are listed than replaced the extra items will insert and not replace existing items
mylist[1:3] = ["kiwi", "watremelon"]
print(mylist)

# Insert after index 2
mylist.insert(2, "blueberry")
print(mylist)

# Append to list
mylist.append("pomegranate")
print(mylist)

# Extend (append a collection to a list)
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)

# Remove list item
mylist.remove("apple")
print(mylist)

# Remove a specific index (removes last index if none is specified
mylist.pop(1)
print(mylist)

# del keyword can be used an alternative to pop
del mylist[0]
print(mylist)

# Empty list of contents
mylist.clear()
print(mylist)

# Loop through a list
mylist = ["apple", "orange", "banana", "strawberry"]
for x in mylist:
 print(x)
 
 # Loop through index numbers
for i in range(len(mylist)):
 print(mylist[i]) 
 
# While loop
i = 0
while i < len(mylist):
 print(mylist[i])
 i = i+1
 
# Compression (shorthand for loop)
[print(x) for x in mylist]
print("----")
# Create a new list with only items with an a in the name
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in mylist  if "b" in x]
print(newlist);

# Sort alphanumerically (ascending by default)
mylist.sort()
print(mylist)

# Sort descending
mylist.sort(reverse = True)
print(mylist)

# Case insensitive sort
mylist.sort(key = str.lower)
print(mylist)

#copy list
mylist2 = mylist.copy()
print(mylist2)
