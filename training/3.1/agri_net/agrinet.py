"""
PROG: agrinet
LANG: PYTHON3
"""

import sys

fin = open("agrinet.in", "r")
fout = open ('agrinet.out', 'w')

N = int(fin.readline())
rawInputs = fin.readlines()
input = []
inputs = []
for rawInput in rawInputs:
    input += list(map(int, rawInput.split()))
    #print(len(input))
    if len(input) == N:
        inputs.append(input)
        input = []

sources = [-1] * N
distances = [0] * N

#print(sources)
#print(distances)

curInd = 0
count = 1
while count < N:
    minDist = sys.maxsize
    minInd = -1
    for i in range(N):
        if sources[i] == -1 and i != 0:
            if i != curInd and minDist > inputs[curInd][i]:
                minDist = inputs[curInd][i]
                minInd = i
            for j in range(N):
                if i != j and minDist > inputs[j][i] and sources[j] != -1:
                    minDist = inputs[j][i]
                    minInd = i
    count += 1
    sources[minInd] = curInd
    curInd = minInd
    distances[minInd] = minDist

#print("distances=", distances)
#print("sources=", sources)

fout.write(str(sum(distances)) + '\n')

fout.close()
