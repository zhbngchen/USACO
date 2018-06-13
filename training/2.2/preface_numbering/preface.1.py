"""
PROG: preface
LANG: PYTHON3

"""
import sys

with open("preface.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])

NUM_LETTERS = 7

symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

# I-1, V-5, X-10, L-50, C-100, D-500, M-1000
#              I  V  X  L  C  D  M
countsOnes = [[1, 0, 0, 0, 0, 0, 0], # I
              [2, 0, 0, 0, 0, 0, 0], # II
              [3, 0, 0, 0, 0, 0, 0], # III
              [1, 1, 0, 0, 0, 0, 0], # IV
              [0, 1, 0, 0, 0, 0, 0], # V
              [1, 1, 0, 0, 0, 0, 0], # VI
              [2, 1, 0, 0, 0, 0, 0], # VII
              [3, 1, 0, 0, 0, 0, 0], # VIII
              [1, 0, 1, 0, 0, 0, 0]] # IX

#              I  V  X  L  C  D  M
countsTens = [[0, 0, 1, 0, 0, 0, 0], # X
              [0, 0, 2, 0, 0, 0, 0], # XX
              [0, 0, 3, 0, 0, 0, 0], # XXX
              [0, 0, 1, 1, 0, 0, 0], # XL
              [0, 0, 0, 1, 0, 0, 0], # L
              [0, 0, 1, 1, 0, 0, 0], # LX
              [0, 0, 2, 1, 0, 0, 0], # LXX
              [0, 0, 3, 1, 0, 0, 0], # LXXX
              [0, 0, 1, 0, 1, 0, 0]] # XC

#               I  V  X  L  C  D  M
countsHunds = [[0, 0, 0, 0, 1, 0, 0], # C
               [0, 0, 0, 0, 2, 0, 0], # CC
               [0, 0, 0, 0, 3, 0, 0], # CCC
               [0, 0, 0, 0, 1, 1, 0], # CD
               [0, 0, 0, 0, 0, 1, 0], # D
               [0, 0, 0, 0, 1, 1, 0], # DC
               [0, 0, 0, 0, 2, 1, 0], # DCC
               [0, 0, 0, 0, 3, 1, 0], # DCC
               [0, 0, 0, 0, 1, 0, 1]] # CM

#               I  V  X  L  C  D  M
countsThous = [[0, 0, 0, 0, 0, 0, 1], # M
               [0, 0, 0, 0, 0, 0, 2], # MM
               [0, 0, 0, 0, 0, 0, 3]] # MMM

totalCountsOnes = [0] * len(countsOnes[0])
for i in range(len(countsOnes)):
  for j in range(len(countsOnes[0])):
    totalCountsOnes[j] += countsOnes[i][j]

totalCountsTens = [0] * len(countsTens[0])
for i in range(len(countsTens)):
  for j in range(len(countsTens[0])):
    totalCountsTens[j] += countsTens[i][j]

totalCountsHunds = [0] * len(countsHunds[0])
for i in range(len(countsHunds)):
  for j in range(len(countsHunds[0])):
    totalCountsHunds[j] += countsHunds[i][j]

print("totalCountsOnes=", totalCountsOnes)
print("totalCountsTens=", totalCountsTens)
print("totalCountsHunds=", totalCountsHunds)

thouN = N // 1000
counts = [0] * NUM_LETTERS
modThouN = N % 1000
if thouN != 0:
  for i in range(NUM_LETTERS):
    counts[i] += totalCountsHunds[i] * thouN * 100
    counts[i] += totalCountsTens[i] * thouN * 100
    counts[i] += totalCountsOnes[i] * thouN * 100
    for j in range(thouN):
      if j != thouN - 1:
        counts[i] += countsThous[j][i] * 1000
      else:
        counts[i] += countsThous[j][i] * (modThouN+1)

hundN = (N % 1000) // 100
modHundN = N % 100
if hundN != 0:
  for i in range(NUM_LETTERS):
    counts[i] += totalCountsTens[i] * hundN * 10
    counts[i] += totalCountsOnes[i] * hundN * 10
    for j in range(hundN):
      if j != hundN - 1:
        counts[i] += countsHunds[j][i] * 100
      else:
        counts[i] += countsHunds[j][i] * (modHundN+1)

tenN = (N % 100) // 10
modTenN = N % 10
if tenN != 0:
  for i in range(NUM_LETTERS):
    counts[i] += totalCountsOnes[i] * tenN
    for j in range(tenN):
      if j != tenN - 1: 
        counts[i] += countsTens[j][i] * 10
      else:
        counts[i] += countsTens[j][i] * (modTenN+1)

oneN = N % 10
if oneN != 0:
  for i in range(NUM_LETTERS):
    for j in range(oneN):
      counts[i] += countsOnes[j][i]

print("counts=", counts)

with open('preface.out', 'w') as fout:
  for i in range(NUM_LETTERS):
    if counts[i] != 0:
      fout.write(str(symbols[i]) + ' ' + str(counts[i]) + '\n')

