"""
PROG: inflate
LANG: PYTHON3
"""

import sys

fin = open("inflate.in", "r")
fout = open ('inflate.out', 'w')

M, N = map(int, fin.readline().split())
inputs = []
minPeriod = sys.maxsize
for i in range(N):
    score, period = map(int, fin.readline().split())
    if minPeriod > period:
        minPeriod = period
    inputs.append([score/period, period, score])
inputs = sorted(inputs, reverse=True)

refinedInputs = []
for rate, period, score in inputs:
    refinedInputs.append([period, score])
    if period == minPeriod:
        break

if inputs[N-1][2] > refinedInputs[len(refinedInputs)-1][1]:
    refinedInputs.append([inputs[N-1][1], inputs[N-1][2]])

#print(refinedInputs)
print(len(refinedInputs))
fin.close()

scores = [0] * (M+1)
indexes = [0] * (M+1)
refinedInputs = sorted(refinedInputs)
for period, score in refinedInputs:
    for i in range(M+1):
        if i < period:
            continue
        curScore = score + scores[i - period]
        if i == M-1:
            print(scores[i], indexes[i])
        if i == 890:
            print(scores[i], indexes[i])
        if curScore > scores[i]:
            scores[i] = curScore

fout.write(str(scores[M]) + '\n')

fout.close()