"""
PROG: wormhole
LANG: PYTHON3

"""

import sys

with open("wormhole.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
holes = []
for i in range(N):
  holes.append(list(map(int, lines[i+1].strip('\n').split())))

#print(N)
#print(holes)

nextHole = []
for i in range(N):
  minNext = ' '
  for j in range(N):
    if i != j and holes[i][1] == holes[j][1] and holes[i][0] < holes[j][0]:
      if minNext == ' ':
        minNext = holes[j][0]
        nextHole.append(j)
      elif minNext > holes[j][0]:
        minNext = holes[j][0]
        nextHole[i] = j
  if minNext == ' ':
    nextHole.append(-1) 

#print(nextHole)    

def checkCircle(start, parings):
  nextMove = start
  for i in range(N+1):
    nextMove = nextHole[nextMove]
    #print("start1=", start, " nextMove=", nextMove)
    if nextMove == -1:
      return False
    else:
      nextMove = parings[nextMove]
      #print("start2=", start, " nextMove=", nextMove)
      if nextMove == -1:
        return False
      elif nextMove == start:
        return True
  return True

def checkParings(parings):
  #print("parings=", parings)
  for i in range(N):
    if checkCircle(i, parings) == True:
      return True
  #print("parings2=", parings)
  return False

parings = [-1] * N
total = 0
def comboHoles(parings):
  ind = -1
  for i in range(N):
    if parings[i] == -1:
      ind = i
      break
  if ind == -1:
    if checkParings(parings):
      global total
      total += 1
    return

  for j in range(ind+1, N):
    if parings[j] == -1:
      parings[ind] = j
      parings[j] = ind
      comboHoles(parings)
      parings[ind] = -1
      parings[j] = -1

comboHoles(parings)
#print("total=", total)

with open('wormhole.out', 'w') as fout:
  fout.write(str(total) + '\n')

