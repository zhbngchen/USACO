"""
PROG: factory
LANG: PYTHON3
"""

import sys

fin = open("factory.in", "r")
fout = open ('factory.out', 'w')

N = int(fin.readline())
matches = [0] * (N+1)
print(matches)
paths = []
for i in range(N+1):
  paths.append([])
for _ in range(N-1):
  a, b = map(int, fin.readline().split())
  matches[a] = b

print(matches)
print(paths)
for i in range(1, N+1):
  if i not in paths[matches[i]] and matches[i] != 0:
    paths[matches[i]].append(i)
    print(paths)
  k = matches[i]
  while matches[k] != 0:
    if i not in paths[matches[k]]:
      paths[matches[k]].append(i)
      print(paths)
    k = matches[k]

print(paths)   

resultFound = False
for i in range(N+1):  
  if len(paths[i]) == N-1:
    fout.write(str(i) + '\n')
    resultFound = True
    break
if resultFound == False:
  fout.write("-1\n")

fout.close()
