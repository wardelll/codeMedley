# tuples are ordered and unchangeable 
# create / pack
mytuple = ("apple", "banana", "cherry")
print(mytuple) 

# access tuple item 
print(mytuple[1])

#convert tuple to list
mylist = list(mytuple)


#update value
mylist[1] = "orange"

#convert back to tuple
mytuple = tuple(mylist)

print(mytuple)

# unpack
(fuji, navel, van) = mytuple 

print(fuji)
print(navel)
print(van)

#multiply  the number of items
doupletuple = mytuple * 2

print(doupletuple)
