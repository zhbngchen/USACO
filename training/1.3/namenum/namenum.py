"""
PROG: namenum
LANG: PYTHON3
"""

import sys

fin = open("namenum.in", "r")
fout = open ('namenum.out', 'w')

fDict = open('dict.txt', 'r')

N = fin.readline().strip()

dictionary = set()
line = fDict.readline().strip()
while line != "":
  dictionary.add(line)
  line = fDict.readline().strip()

lettersFromNum = { \
    '2':['A', 'B', 'C'], \
    '3':['D', 'E', 'F'], \
    '4':['G', 'H', 'I'], \
    '5':['J', 'K', 'L'], \
    '6':['M', 'N', 'O'], \
    '7':['P', 'R', 'S'], \
    '8':['T', 'U', 'V'], \
    '9':['W', 'X', 'Y']}

def findNames(number, i, name, result):
  if i == len(number):
    if name in dictionary:
      result.append(name)
    return
  else:
    localName = name
    for letter in lettersFromNum[number[i]]:
      name = localName
      name += letter
      findNames(number, i+1, name, result)

name = ''
result = []
findNames(N, 0, name, result)

if not result:
  fout.write("NONE" + '\n')
else:
 for eachResult in result:
   fout.write(str(eachResult) + '\n')
  
fout.close()
