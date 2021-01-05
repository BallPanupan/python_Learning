def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)

"""
10 + tri_recursion(9)                     10 + 9 + 45 = 55
  9 + tri_recursion(8)                    9 + 8 + 28 = 45
    8 + tri_recursion(7)                  8 + 7 + 21 = 36
      7 + tri_recursion(6)                7 + 6 + 15 = 28
        6 + tri_recursion(5)              6 + 5 + 10 = 21
          5 + tri_recursion(4)            5 + 4 + 6 = 15
            4 + tri_recursion(3)          4 + 3 + 3 = 10
              3 + tri_recursion(2)        3 + 2 + 1 = 6
                2 + tri_recursion(1)      2 + 1 + 0 = 3
                  1 + tri_recursion(0)    1 + 0 + 0 = 1
                    0 + tri_recursion(0)  0 + 0 + 0 = 0

result:
1
3
6
10
15
21
28
36
45
55
"""