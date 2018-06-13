"""
PROG: runround
LANG: PYTHON3

"""
import sys

with open("runround.in", "r") as fin:
  lines = fin.readlines()

M = int(lines[0])

print(M)

def checkUnique(value):
  strValue = str(value)
  setCharValue = set(strValue)
  if '0' in strValue:
    return False
  return len(setCharValue) == len(strValue)

def checkRunRound(value):
  strVal = str(value)
  listVal = []
  for d in strVal:
    listVal.append(int(d))
  lenListVal = len(listVal)
  counts = [0] * lenListVal

  index = 0
  while counts[index] == 0:
    counts[index] = 1
    index += listVal[index]
    if index >= lenListVal:
      index = index % lenListVal

  if index == 0:
    found = True
    for count in counts:
      if count == 0:
        found = False
        break
    return found
  else:
    return False

value = M
while True:
  value += 1
  if checkUnique(value) == False:
    continue
  if checkRunRound(value):
    break

with open('runround.out', 'w') as fout:
  fout.write(str(value) + '\n')


