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

counts = [0] * NUM_LETTERS
for i in range(N+1):
  print("i=", i)
  thouN = i // 1000
  if thouN != 0:
    for j in range(NUM_LETTERS):
      counts[j] += countsThous[thouN-1][j]
  hundN = (i % 1000) // 100
  if hundN != 0:
    for j in range(NUM_LETTERS):
      counts[j] += countsHunds[hundN-1][j]
  tenN = (i % 100) // 10
  if tenN != 0:
    print("tenN=", tenN)
    for j in range(NUM_LETTERS):
      counts[j] += countsTens[tenN-1][j]
  oneN = i % 10
  if oneN != 0:
    print("oneN=", oneN)
    for j in range(NUM_LETTERS):
      counts[j] += countsOnes[oneN-1][j]

print("counts=", counts)

with open('preface.out', 'w') as fout:
  for i in range(NUM_LETTERS):
    if counts[i] != 0:
      fout.write(str(symbols[i]) + ' ' + str(counts[i]) + '\n')

