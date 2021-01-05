x = 5
y = "John"
print(x)
print(y)

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#Unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#Output Variables
x = "awesome"
print("Python is " + x)

#Global Variables
x = "Output Variables"
def myfunc():
  print("Python is " + x)

myfunc()

#If you use the global keyword, the variable belongs to the global scope:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
