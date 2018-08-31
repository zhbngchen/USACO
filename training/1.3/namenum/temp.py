import sys

def fibonaci(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  return fibonaci(n-1) + fibonaci(n-2)

retVal = fibonaci(5)
print("fibonaci(5): ", retVal)

