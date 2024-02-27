# dictionaries are ordered, changeable, and don't allow duplicates

# create

mydict = {
	"brand": "Chevy",
	"model": "Corvette",
	"year": 1957
}
print(mydict)

thisdict = dict(name = "Bob", age = 30, country = "Canada")
print(thisdict)

# reference by key
print(mydict["brand"])

# retern dictionary items as a list of tuples
myitems = mydict.items()
print(myitems)

# add item 
mydict["color"] = "black"
print(mydict)

# remove item
del mydict["color"]
print(mydict)
