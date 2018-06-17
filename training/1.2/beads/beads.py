"""
PROG: beads
LANG: PYTHON3
"""

import sys

fin = open("beads.in", "r")
fout = open ('beads.out', 'w')

N = int(fin.readline())
inBeads = fin.readline().rstrip()
print("inBeads=", inBeads)
print("len(inBeads)=", len(inBeads))

def singularBeads(beads):
  lastNonW = ''
  for bead in beads:
    if bead != 'w':
      if lastNonW == '':
        lastNonW = bead
      elif bead != lastNonW:
        return False
  return True

def singleOccuNonW(beads):
  firstNonW = ''
  secondNonW = ''
  for bead in beads:
    if bead != 'w':
      if firstNonW == '':
        firstNonW = bead
      elif secondNonW == '':
        secondNonW = bead
      else:
        return False
  return True

def combineSameBeads(beads, counts):
  newBeads = []
  newCounts = []
  count = counts[0]
  for i in range(1, len(beads)):
    if beads[i] == beads[i-1]:
      count += counts[i]
    else:
      newBeads.append(beads[i-1])
      newCounts.append(count)
      count = counts[i]
  newBeads.append(beads[len(beads)-1])
  newCounts.append(count)
  return newBeads, newCounts

def findMax(beads):
  inBeads = beads + beads

  beadList1 = []
  countList1 = []
  for i in range(0, len(inBeads)):
    beadList1.append(inBeads[i])
    countList1.append(1)
  print("beadList1=", beadList1)
  print("countList1=", countList1)

  beadList2, countList2 = combineSameBeads(beadList1, countList1)
  print("beadList2=", beadList2)
  print("countList2=", countList2)

  # change w to r/b if previous and after are the same
  for i in range(1, len(beadList2) - 1):
    if beadList2[i] == 'w' and beadList2[i-1] == beadList2[i+1]:
      beadList2[i] = beadList2[i-1]

  print("after beadList2=", beadList2)
  print("after countList2=", countList2)

  beadList3, countList3 = combineSameBeads(beadList2, countList2)
  print("beadList3=", beadList3)
  print("countList3=", countList3)

  # adding w and 0 in between b and r if no w between b and r (to generalize next step handling)
  beadList4 = []
  countList4 = []
  for i in range(len(beadList3) - 1):
    beadList4.append(beadList3[i])
    countList4.append(countList3[i])
    if beadList3[i] != 'w' and beadList3[i+1] != 'w':
      beadList4.append('w')
      countList4.append(0)
  beadList4.append(beadList3[len(beadList3) - 1])
  countList4.append(countList3[len(beadList3) - 1])

  print("beadList4= ", beadList4)
  print("countList4= ", countList4)

  # Move non-zero w's to neighboring b/r by comparing sum of previous 4 and next 4
  for i in range(len(beadList4)):
    if beadList4[i] == 'w':
      if i == 0:
        countList4[i+1] += countList4[i]
        countList4[i] = 0
        continue
      else:
        if i >= 4:
          lowIndex = i - 4
        else:
          lowIndex = 0
        sumBefore = 0
        for j in range(lowIndex, i):
          sumBefore += countList4[j]
      if i == len(beadList4) - 1:
        countList4[i-1] += countList4[i]
        countList4[i] = 0
        continue
      else:
        if i + 4 < len(beadList4):
          upIndex = i + 4
        else:
          upIndex = len(beadList4) - 1
        sumAfter = 0
        for j in range(i+1, upIndex + 1):
          sumAfter += countList4[j]
      if sumBefore > sumAfter:
        countList4[i-1] += countList4[i]
      else:
        countList4[i+1] += countList4[i]
      countList4[i] = 0

  print("after beadList4= ", beadList4)
  print("after countList4= ", countList4)
  print("after len beadList4= ", len(beadList4))

  # remove w and 0
  beadList5 = []
  countList5 = []
  for i in range(0, len(beadList4)):
    if beadList4[i] != 'w':
      beadList5.append(beadList4[i])
      countList5.append(countList4[i])

  print("beadList5=", beadList5)
  print("countList5=", countList5)
  result = 0
  for i in range(0, len(beadList5) - 1):
    count = countList5[i] + countList5[i+1]
    if result < count:
      result = count

  print("result=", result)
  return result

if singularBeads(inBeads) or singleOccuNonW(inBeads):
  result = N
else:
  result = findMax(inBeads)

if result > N:
  result = N

fout.write(str(result) + '\n')
  
fout.close()
