"""
PROG: palsquare
LANG: PYTHON3
"""

import sys

bases = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

lowest = 1
highest = 300

with open("palsquare.in") as fin:
  B = int(fin.readline())

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

with open("palsquare.out", "w") as fout:
  for i in range(lowest, highest + 1):
    strNum = numberWithBase(i*i, B)
   # print("i=", i, " strNum=", strNum)
    if isPalindrome(strNum):
      iInBase = numberWithBase(i, B)
      fout.write(str(iInBase) + ' ' + strNum + '\n')

