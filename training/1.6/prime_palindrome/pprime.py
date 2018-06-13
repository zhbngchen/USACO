"""
PROG: pprime
LANG: PYTHON3

"""
import sys
import math

with open("pprime.in", "r") as fin:
  lines = fin.readlines()

minNum, maxNum = map(int, lines[0].split())

def preprocessNum(num):
  numDigits = 0
  leftMost = num
  while(num > 0):
    leftMost = num
    num = num // 10
    numDigits += 1
  return numDigits, leftMost

minNumDigits, leftMostMin = preprocessNum(minNum)
maxNumDigits, leftMostMax = preprocessNum(maxNum)

"""
def isPrime(num):
  for x in range(2, int(math.sqrt(num))+1):
    if num % x == 0:
      return False
  return True
"""
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

#print("minNumDigits=", minNumDigits, " leftMostMin=", leftMostMin, " maxNumDigits=", maxNumDigits, " leftMostMax=", leftMostMax)

def formPalindrome(i, numLoop, numDigits, number, results, minNum, minNumDigits, leftMostMin, maxNum, maxNumDigits, leftMostMax):
  if i == numLoop:
    if isPrime(number) and number >= minNum and number <= maxNum:
      results.append(number)
    #print("append results=", results)
    number = 0
    return
  #print("i=", i, " numLoop=", numLoop, " numDigits=", numDigits, " number=", number, " minNum=", minNum, " maxNum=", maxNum)
  if i == 0:
    digits = [1, 3, 7, 9]
  else:
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  for digit in digits:
    if i == 0:
      if minNumDigits == True and digit < leftMostMin:
        continue
      elif maxNumDigits == True and digit > leftMostMax:
        continue
    if i != numLoop-1 or numDigits%2 == 0:
      number += digit*(10**(numDigits-1-i)) + digit*(10**i)
    else:
      number += digit*(10**i)
    #print("number=", number, " digit=", digit)
    formPalindrome(i+1, numLoop, numDigits, number, results, minNum, minNumDigits, leftMostMin, maxNum, maxNumDigits, leftMostMax)
    if i!= numLoop-1 or numDigits%2 == 0:
      number -= digit*(10**(numDigits-1-i)) + digit*(10**i)
    else:
      number -= digit*(10**i)

results = []
for numDigits in range(minNumDigits, maxNumDigits+1):
  if numDigits%2 == 0:
    numLoop = numDigits//2
  else:
    numLoop = numDigits//2 + 1
  if numDigits ==1:
    digits = [2, 3, 5, 7]
    for digit in digits:
      if digit >= minNum:
        results.append(digit)
  else:
    number = 0
    formPalindrome(0, numLoop, numDigits, number, results, minNum, numDigits == minNumDigits, leftMostMin, maxNum, numDigits == maxNumDigits, leftMostMax)

with open('pprime.out', 'w') as fout:
  for result in results:
    fout.write(str(result) + '\n')
