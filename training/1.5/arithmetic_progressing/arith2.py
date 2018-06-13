"""
PROG: ariprog
LANG: PYTHON3

"""

import sys
import operator

with open("ariprog.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
M = int(lines[1])

#print(N)
#print(M)

bisquares = [0] * ((M+1)*(M+1)*2 + 1)
for i in range(M+1):
  for j in range(M+1):
    bisquares[i*i + j*j] = 1

#bisquares = list(set(bisquares))
#print("len bisquares: ", len(bisquares))
#print("bisquares: ", bisquares)

maxB = M*M*2 // (N-1)
#print(maxB)

results = []
for i in range(len(bisquares)):
  if bisquares[i] != 0:
    for j in range(1, maxB+1, 1):
      found = True
      if (i+j*(N-1)) > len(bisquares):
        found = False
        #print("1i=", i, " j=", j, " maxB=", maxB, " bisquares=", bisquares[i])
        break
      for k in range(N):
        if bisquares[i+j*k] == 0:
          found = False
          #print("2i=", i, " j=", j, " maxB=", maxB, " bisquares=", bisquares[i])
          break
      if found == True:
        #print("3i=", i, " j=", j, " maxB=", maxB, " bisquares=", bisquares[i])
        results.append([j, i])

results.sort()

with open('ariprog.out', 'w') as fout:
  if len(results) == 0:
    fout.write('NONE' + '\n')
  else:
    for result in results:
      fout.write(str(result[1]) + ' ' + str(result[0]) + '\n')


