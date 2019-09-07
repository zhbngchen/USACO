"""
PROG: fence
LANG: PYTHON3

"""
import sys

with open("fence.in", "r") as fin:
  lines = fin.readlines()

F = int(lines[0])
inputs = {}

sys.setrecursionlimit(1500)

for i in range(1, F+1):
  i, j = map(int, lines[i].split())
  if i not in inputs.keys():
    inputs[i] = []
  inputs[i].append(j)
  if j not in inputs.keys():
    inputs[j] = []
  inputs[j].append(i)

#print(inputs)

lowPoint = 501
for i in inputs.keys():
  if len(inputs[i]) % 2 != 0:
    if i < lowPoint:
      lowPoint = i

if lowPoint == 501:
  lowPoint = min(inputs.keys())

#print("lowPoint=", lowPoint)

def findPath(results, inputs, point):
  if len(inputs[point]) == 0:
    results.append(point)
    return
  while len(inputs[point]) != 0:
    minPoint = min(inputs[point])
    inputs[point].remove(minPoint)
    inputs[minPoint].remove(point)
    findPath(results, inputs, minPoint)
  results.append(point)

results = []
findPath(results, inputs, lowPoint)

with open('fence.out', 'w') as fout:
  for i in range(len(results)-1, -1, -1):
    fout.write(str(results[i]) + '\n')