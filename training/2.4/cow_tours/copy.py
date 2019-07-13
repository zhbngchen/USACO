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
#printList(coordinates)
print("matrix0=")
#printList(matrix0)

print("connecting points: ")
for i in range(N):
  for j in range(N):
    if matrix0[i][j] == 1 and i == 114:
      print("(", i, ", ", j, "), ")

def calcDistance(coord, i, j):
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
      row.append(calcDistance(matrix0, i, j))
  distanceMatrix.append(row)

print("distanceMatrix[114]=", distanceMatrix[114])
#printList(distanceMatrix)

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
               if modified == True and (i == 114 and j == 12) or (i == 12 and j == 81):
                  print("modified i=", i, ", j=", j, ", distanceMatrix[i][j]=", distanceMatrix[i][j], ", k=", k, ", distanceMatrix[i][k]=", distanceMatrix[i][k], ", distanceMatrix[k][j]=", distanceMatrix[k][j])
                  #printList(distanceMatrix)

print("after distanceMatrix[114]=", distanceMatrix[114])

maxFromPoints = [0 for i in range(N)]
for i in range(N):
  maxPerRow = -1
  for j in range(N):
    if maxPerRow < distanceMatrix[i][j]:
      maxPerRow = distanceMatrix[i][j]
      if i == 114:
        print("i=114, j=", j, "distanceMatrix[114][j]=", distanceMatrix[i][j])
      maxFromPoints[i] = maxPerRow

print("maxFromPoints[114]=", maxFromPoints[114])

result = sys.float_info.max
for i in range(N):
  for j in range(N):
    if i != j and distanceMatrix[i][j] == 0:
      curDistance = maxFromPoints[i] + maxFromPoints[j] + calcDistance(matrix0, i, j)
      if curDistance < result:
        result = curDistance
        print("i=", i, ", j=", j, "maxFromPoints[i]=", maxFromPoints[i], "maxFromPoints[j]=", maxFromPoints[j], "result=", result)

if result < max(maxFromPoints):
  result = max(maxFromPoints)

with open('cowtour.out', 'w') as fout:
  fout.write(f'{result:.6f}' + '\n')