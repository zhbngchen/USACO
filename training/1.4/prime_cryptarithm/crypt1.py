"""
PROG: crypt1
LANG: PYTHON3
"""

import sys

fin = open("crypt1.in", "r")
fout = open ('crypt1.out', 'w')

N = int(fin.readline())
numbers = list(set(list(fin.readline().split())))

#Return False is len(z)>=count or z contains number outside numbers
def isCrypt(z, count, numbers):
  if len(str(z)) >= count:
    return False
  for l in str(z):
    if l not in numbers:
      return False
  return True

""" solution #1 -- no-recursion
combos = ['']
L = len(numbers)
for i in range(5):
  combos *= L
  n = len(combos) // L
  index = 0
  for num in numbers:
    for i2 in range(n):
      combos[index] += num
      index += 1

count = 0
for combo in combos:
  x = combo[0:3]
  y1 = combo[3]
  y2 = combo[4]
  z = int(x) * int(y1 + y2)
  if isCrypt(z, 5, numbers) == False:
    continue
  z1 = int(x) * int(y1)
  if isCrypt(z1, 4, numbers) == False:
    continue
  z2 = int(x) * int(y2)
  if isCrypt(z2, 4, numbers) == False:
    continue
  count += 1
"""

# Following is the recursion version
count = 0
def checkCrypt(i, combo):
  if i == 5:
    #print(combo)
    x = combo[0:3]
    y1 = combo[3]
    y2 = combo[4]
    z = int(x) * int(y1 + y2)
    if isCrypt(z, 5, numbers) == False:
      return
    z1 = int(x) * int(y1)
    if isCrypt(z1, 4, numbers) == False:
      return
    z2 = int(x) * int(y2)
    if isCrypt(z2, 4, numbers) == False:
      return
    global count
    count += 1
    return
    
  for ch in numbers:
    copyCombo = combo
    combo += ch
    checkCrypt(i+1, combo)
    combo = copyCombo

checkCrypt(0, '')

#print(count)
fout.write(str(count) + '\n')

fout.close()

