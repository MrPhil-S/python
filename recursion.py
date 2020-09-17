

#function for fibinachi sequence
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fib(n-1) + fib (n-2)

#  1 2 3 4 5 6  7  8  9 10
#0,1,1,2,3,5,8,13,21,34,45
print(fib(10))
