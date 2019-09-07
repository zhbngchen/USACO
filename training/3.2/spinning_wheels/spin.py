"""
PROG: spin
LANG: PYTHON3
"""

import sys
with open('spin.in', 'r') as fin:
  lines = fin.readlines()

speeds = []
wedges = [[0 for _ in range(360)] for _ in range(5)]

for i in range(5):
    vals = list(map(int, lines[i].split()))
    speeds.append(vals[0])
    for j in range(vals[1]):
        for k in range(vals[2+j*2+1]+1): #last +1 is due to inclusive
            wedges[i][int((vals[2+j*2]+k)%360)] = 1

startPos = [0 for _ in range(5)]
records = set()
result = 0
found = False
while True:
    for j in range(360):
        for i in range(5):
            if wedges[i][int((j+startPos[i])%360)] == 0:
                break
            if i == 4:
                found = True
                break
    if found == True:
        break
    result += 1
    for i in range(5):
        startPos[i] = int((startPos[i] + 360 - speeds[i])%360) #since the wedges' angle grows with speed, the startPos actually drop with speed
    lTuple = tuple(startPos)
    if lTuple not in records:
        records.add(lTuple)
    else:
        break

with open('spin.out', 'w') as fout:
    if found != True:
        fout.write("none\n")
    else:
        fout.write(str(result) + '\n')
    