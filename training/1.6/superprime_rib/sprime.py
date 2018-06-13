"""
PROG: sprime
LANG: PYTHON3

"""
import sys
import math

with open("sprime.in", "r") as fin:
  lines = fin.readlines()

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 

N = int(lines[0])

firstDigits = [2, 3, 5, 7]
lastDigits = [1, 3, 7, 9]

def solve(i, N, firstDigits, lastDigits, number, results):
  if i == N:
    if isPrime(number):
      results.append(number)

  if i == 0:
    for digit in firstDigits:
      number = digit
      solve(i+1, N, firstDigits, lastDigits, number, results)
  else:
    for digit in lastDigits:
      number *= 10
      number += digit
      if isPrime(number):
        solve(i+1, N, firstDigits, lastDigits, number, results)
        number = number // 10
      else:
        number = number // 10
        continue

results = []
number = 0
solve(0, N, firstDigits, lastDigits, number, results)

with open('sprime.out', 'w') as fout:
  for result in results:
    fout.write(str(result) + '\n')
