# set are unordered 
# set items are unchageable but can be added or removed and don't allow duplicate vlues

# create a set 
myset = {"apple", "banna", "cherry"}
print(myset)

settwo = set(("one","two","three"))
print(settwo)

# add items 
myset.add("ornge")
print(myset)

# add set (works with any collection)
myset.update(settwo)
print(myset)

# remove item
myset.remove("apple")
print(myset)

# wont raise an error if the item doesn't exist
myset.discard("apple")
print(myset)

# use two sets to create a new set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# keep only duplicates
first = {"apple", "orange", "banna"}
second = {"red", "orange", "yellow"}

first.intersection_update(second)
print(first)

first = {"apple", "orange", "banna"}
second = {"red", "orange", "yellow"}

third = first.intersection(second)
print(third)

# keep all but duplicates 
first = {"apple", "orange", "banna"}
second = {"red", "orange", "yellow"}

first.symmetric_difference_update(second)
print(first)

first = {"apple", "orange", "banna"}
second = {"red", "orange", "yellow"}

third = first.symmetric_difference(second)
print(first)
