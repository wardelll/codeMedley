# if else
x=55
y=33
if x > y:
	print("this is greater than that") 
elif x == y:
	print ("this is equal to that")
else:
	print("this is not greater than that")
	
# shorthand 
print("x") if x > y else print("=") if x == y else print("y")

# while loop

i = 1
while i < 8:
  print(i)
  i += 1
  
# break
i = 1
while i < 8:
  print(i)
  if i == 4:
    break
  i += 1
  
# continue 
i = 0
while i < 8:
  i += 1
  if i == 4:
    continue
  print(i)
  
# while else

i = 1
while i < 8:
  print(i)
  i += 1
else:
  print("i is no longer less than 8")
  
  
# range (default start value is 0, default inrement is 1)
for x in range(8):
  print(x)
  
# range with start value
for x in range(2, 8):
  print(x)
  
# increment by 2 
for x in range(1, 8, 2):
  print(x)
  
# for else 
for x in range(8):
  print(x)
else:
  print("Done!")
