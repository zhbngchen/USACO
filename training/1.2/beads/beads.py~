"""
PROG: beads
LANG: PYTHON3
"""

import sys

fin = open("beads.in", "r")
fout = open ('beads.out', 'w')

N = int(fin.readline())
inBeads = fin.readline().rstrip()

"""
Create list of single bead and count
"""
beads = []
counts = []
curBead = ' '
count = 1
for bead in inBeads:
  if curBead != bead:
    if curBead != ' ':
      beads.append(curBead)
      counts.append(count)
      curBead = bead
      count = 1
    else:
      curBead = bead
  else:
    curBead = bead
    count += 1
beads.append(curBead)
counts.append(count)

print(beads)
print(counts)

print("len of bead2:", len(beads))

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

def findMax(beads, counts):
  """
  w is the special character
  b and r are interchangeable

  Scenarios are:
  case1:	x[wx]*y : following many wx need to be combined into x, store at y
  case2:	xwy : store x and then store w, store at y, later w will be considered to either x or y 
  case3:	^wx : begin with w, w needs to be applied to x 
  case4:	xw$ : end with w, w needs to be applied to x
  Design:
	lastNonW : remember x
	count : counting how many x and several wx 
	countLastW : remember w's count in case2 to be applied to y later
  """
  beads2 = []
  counts2 = []
  lastNonW = ''
  countLastW = 0
  index = 0
  while index < len(beads):
    if beads[index] != 'w':
      if beads[index] == lastNonW:
        count += counts[index] + countLastW
        countLastW = 0
      else:
        if lastNonW != '':
          beads2.append(lastNonW)
          counts2.append(count)
          if countLastW != 0:
            beads2.append('w')
            counts2.append(countLastW)
        lastNonW = beads[index]
        count = counts[index]
        countLastW = 0
    else:
      countLastW = counts[index]
    index += 1
  beads2.append(lastNonW)
  counts2.append(count)

  print("beads2=", beads2)
  print("counts2=", counts2)

  maxBeads = 0
  if len(counts2) == 1:
    maxBeads = int(counts2[0] / 2)
  else:
  """
  when current is x, the possible scenarios are wxwyw
  """
    index = 0
    while index < len(counts2):
      count = 0
      if beads2[index] != 'w':
        #index is in position of x
        if index-1 >= 0 and beads2[index-1] == 'w':
          count += counts2[index-1]
        index2 = index + 1
        if index2 < len(counts2) and beads2[index2] == 'w':
          count += counts2[index2]
          index2 += 1
        if index2 >= len(counts2):
          break
        count += counts2[index2]
        if index2+1 < len(counts2) and beads2[index2+1] == 'w':
          count += counts2[index2+1]
        count += counts2[index]
        if maxBeads < count:
          maxBeads = count
        #index2 is in position of y
        index = index2
      else:
        index += 1
    if maxBeads < count:
      maxBeads = count
  return maxBeads

if singularBeads(beads) or singleOccuNonW(beads):
  result = N
else:
  result = findMax(beads * 2, counts * 2)
fout.write(str(result) + '\n')
  
fout.close()
