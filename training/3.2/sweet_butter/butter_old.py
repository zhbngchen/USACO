"""
PROG: butter
LANG: PYTHON3

"""
import sys
import queue

with open('butter.in', 'r') as fin:
  lines = fin.readlines()

N, P, C = map(int, lines[0].split())

pastures = []
for i in range(N):
    pastures.append(int(lines[i+1])-1)

w = [[sys.maxsize for _ in range(P)] for _ in range(P)]

for i in range(C):
    p1, p2, lenP = map(int, lines[N+1+i].split())
    p1n = p1 - 1
    p2n = p2 -1
    w[p1n][p2n] = lenP
    w[p2n][p1n] = lenP
    
for i in range(P):
    w[i][i] = 0

for k in range(P):
    for i in range(P):
        for j in range(P):
            if i != j and w[i][k] != 0 and w[j][k] != 0 and (w[i][j] == 0 or w[i][j] > w[i][k] + w[j][k]):
                w[i][j] = w[i][k] + w[j][k]

result = sys.maxsize
for i in range(P):
    totalLen = 0
    for pasture in pastures:
        totalLen += w[i][pasture]
    if result > totalLen:
        result = totalLen
        print("i=", i)

with open('butter.out', 'w') as fout:
    fout.write(str(result) + '\n')