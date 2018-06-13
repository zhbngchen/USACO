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

bisquares = []
for i in range(M+1):
  for j in range(M+1):
    bisquares.append(i*i + j*j)

bisquares = list(set(bisquares))
print("len bisquares: ", len(bisquares))
print("bisquares: ", bisquares)

maxB = M*M*2 // (N-1)
print(maxB)

maxA = M*M*2 - N
print(maxA)

lists = []
lists.append(list(i for i in range(1, maxB+1)))
lists.append(list(i for i in range(maxA+1)))
print("lists:", len(lists[0]), " and ", len(lists[1]))

cand = [0, 0]
results = []

def searchResult(N, ind):
  if ind == len(lists):
    found = True
    for i in range(N-1, -1, -1):
      sumCand = cand[1] + i*cand[0]
      #if cand[1] == 5 and cand[0] == 20:
        #print("i=", i, " sumCand=", sumCand)
      #print("sumCand=", sumCand, " cand1=", cand[1], " cand0=", cand[0], " i=", i)
      if sumCand not in bisquares:
        found = False
        break
    if found == True:
      results.append([cand[1], cand[0]])
    return
  for i in range(len(lists[ind])):
    cand[ind] = lists[ind][i]
    searchResult(N, ind+1)

searchResult(N, 0)
with open('ariprog.out', 'w') as fout:
  if len(results) == 0:
    fout.write('NONE' + '\n')
  else:
    for result in results:
      fout.write(str(result[0]) + ' ' + str(result[1]) + '\n')


