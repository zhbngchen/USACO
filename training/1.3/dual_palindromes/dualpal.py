"""
PROG:dualpal 
LANG: PYTHON3
"""

import sys

with open('dualpal.in') as fin:
  N, S = map(int, fin.readline().split())


def isPalindrome(stringNum):
  for i in range(len(stringNum)//2):
    if stringNum[i] != stringNum[len(stringNum)-1-i]:
      return False
  return True

def numberWithBase(value, base):
  retStr = ''
  while value >= base:
    retStr = bases[value % base] + retStr
    value = value // base

  retStr = bases[value % base] + retStr
  return retStr

bases = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

count = 0
number = S + 1
result = []
while count < N:
  palindromeCount = 0
  for base in range(2, 11):
    numStr = numberWithBase(number, base)
    #print("number=", number, " base=", base, " numStr=", numStr)
    if isPalindrome(numStr):
      palindromeCount += 1
      if palindromeCount == 2:
        result.append(number)
        count += 1
        break
  number += 1

with open('dualpal.out', 'w') as fout:
  for res in result:
    fout.write(str(res) + '\n')

