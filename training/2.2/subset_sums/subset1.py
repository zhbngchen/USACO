"""
PROG: subset
LANG: PYTHON3

"""
import sys

def findComboCounts(ind, subset, sizeCombo, valCombo, strValCombo, maxValCombo, countsCombo):
  if ind == sizeCombo:
    countsCombo[valCombo - 1] += 1
    #print("valCombo=", valCombo, " strValCombo=", strValCombo)
    return
  elif ind >= len(subset):
    return
  for i in range(ind, len(subset)):
    valCombo += subset[i]
    strValCombo += str(subset[i])
    #print("before i=", i, " ind=", ind, " subset[i]=", subset[i], " strValCombo=", strValCombo)
    if valCombo > maxValCombo:
      valCombo -= subset[i]
      strValCombo = strValCombo[:-1]
      #print("return i=", i, " ind=", ind, " subset[i]=", subset[i], " strValCombo=", strValCombo)
      return
    findComboCounts(i+1, subset, sizeCombo, valCombo, strValCombo, maxValCombo, countsCombo)
    valCombo -= subset[i]
    strValCombo = strValCombo[:-1]
    #print("after i=", i, " ind=", ind, " subset[i]=", subset[i], " strValCombo=", strValCombo)

with open("subset.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
print("N=", N)

sumVal = 0
for i in range(N+1):
  sumVal += i

result = 0
if sumVal%2 == 0:
  halfSum = sumVal//2
  print("halfSum=", halfSum)

  subset1 = []
  countDown = halfSum
  i = N
  while countDown > i:
    subset1.insert(0, i)
    countDown -= i
    i -= 1
  if countDown != 0:
    subset1.insert(0, countDown)
  print(subset1)

  subset2 = []
  for i in range(1, N+1):
    if i not in subset1:
      subset2.append(i)
  print("subset2=", subset2)

  # In order to avoid double counting of subset, remove highest value of subset1 
  maxVal = subset1.pop()

  maxValCombo = halfSum - maxVal
  countsCombo1 = [0] * maxValCombo
  for i in range(len(subset1)):
    valCombo = 0
    strValCombo = ''
    findComboCounts(0, subset1, i+1, valCombo, strValCombo, maxValCombo, countsCombo1)
  print("countsCombo1=", countsCombo1)

  countsCombo2 = [0] * maxValCombo
  for i in range(len(subset2)):
    valCombo = 0
    strValCombo = ''
    findComboCounts(0, subset2, i+1, valCombo, strValCombo, maxValCombo, countsCombo2)
  print("countsCombo2=", countsCombo2)

  result = 1 # counting original subset1 and subset2
  for i in range(maxValCombo):
    result += countsCombo1[i] * countsCombo2[i]
  print("result=", result)

with open('subset.out', 'w') as fout:
  fout.write(str(result) + '\n')

