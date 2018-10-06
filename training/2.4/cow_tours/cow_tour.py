"""
PROG: cowtour
LANG: PYTHON3
"""

import sys
import math

with open('cowtour.in', 'r') as fin:
  lines = fin.readlines()

N = int(lines[0])

coordinates = []

for i in range(1, N+1):
  x, y = map(int, lines[i].split())
  coordinates.append([x, y])

matrix0 = []
for i in range(N+1, 2*N + 1):
  row = []
  for j in range(N):
    row.append(int(lines[i][j]))
  matrix0.append(row)

def printList(a):
  for b in a:
    print(b)

print("N=", N)
print("coordinates=")
printList(coordinates)
print("matrix0=")
printList(matrix0)

def findCoord(coord, i, j):
  d1 = coordinates[i][0] - coordinates[j][0]
  d2 = coordinates[i][1] - coordinates[j][1]
  d1 = d1*d1
  d2 = d2*d2
  return math.sqrt(d1+d2)

distanceMatrix = []
for i in range(N):
  row = []
  for j in range(N):
    if matrix0[i][j] == 0:
      row.append(0)
    else:
      row.append(findCoord(matrix0, i, j))
  distanceMatrix.append(row)

print("distanceMatrix=")
printList(distanceMatrix)

modified = True
while modified == True:
  modified = False
  for i in range(N):
    for j in range(N):
      if distanceMatrix[i][j] == 0 and i != j:
        for k in range(N):
          if distanceMatrix[i][k] != 0 and distanceMatrix[k][j] != 0:
            if distanceMatrix[i][j] == 0 or distanceMatrix[i][j] > (distanceMatrix[i][k] + distanceMatrix[k][j]):
               distanceMatrix[i][j] = distanceMatrix[i][k] + distanceMatrix[k][j]
               modified = True
  if modified == True:
    print("distanceMatrix=")
    printList(distanceMatrix)

index = 1
found = False
while not found:
  for i in range(index):
    print("check index=", index, " i=", i, " found=", found)
    if distanceMatrix[index][i] != 0:
      break
    if i == index-1:
      print("change found to True")
      found = True
  index += 1
    
print("index=", index)

diameter1 = 0
diameter2 = 0
maxDist = []
for i in range(N):
  value = 0
  for j in range(N):
    if distanceMatrix[i][j] > value:
      value = distanceMatrix[i][j]
    if i < index and j < index:
      if distanceMatrix[i][j] > diameter1:
        diameter1 = distanceMatrix[i][j]
    else:
      if distanceMatrix[i][j] > diameter2:
        diameter2 = distanceMatrix[i][j]
  maxDist.append(value)

print("diameter1=", diameter1)
print("diameter2=", diameter2)
print("maxDist=", maxDist)

result = 10000000
print("result=", result)
for i in range(index):
  for j in range(index, N):
    distIJ = findCoord(coordinates, i, j)
    maxIJ = distIJ + maxDist[i] + maxDist[j]
    if maxIJ < result:
      result = maxIJ

if result < max(diameter1, diameter2):
  result = max(diamter1, diameter2)
print("result=", result)

fout = open ('cowtour.out', 'w')
fout.close
