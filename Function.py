def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function2(fname, lname):
  print(fname + " " + lname)

my_function2("Emil", "Refsnes")

def my_function3(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function3(fruits)

def my_function4(x):
        return x * (x-1)

print(my_function4(5))


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    #result = 0
    #return result

    print("\n\nRecursion Example Results")
tri_recursion(6)