"""
PROG: milk
LANG: PYTHON3
"""

import sys

fin = open("milk.in", "r")
fout = open ('milk.out', 'w')

N, M = map(int, fin.readline().split())
details = []
for i in range(M):
  P, A = map(int, fin.readline().split())
  details.append([P, A])

details.sort()
#print(details)

totalCost = 0
index = 0
while N > 0:
  if N > details[index][1]:
    totalCost += details[index][0] * details[index][1]
    N -= details[index][1]
  else:
    totalCost += details[index][0] * N
    N = 0
  index += 1
  if index == len(details):
    break

fout.write(str(totalCost) + '\n')
  
fout.close()
