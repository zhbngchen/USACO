"""
PROG: combo
LANG: PYTHON3

"""

import sys

with open("combo.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
comboJ = list(map(int, lines[1].strip('\n').split()))
comboM = list(map(int, lines[2].strip('\n').split()))

#print(N)
#print(comboJ)
#print(comboM)

def roundVal(value):
  val = value % N
  if val == 0:
    val = N
  return val

def expandCombo(combo):
  expanded = []
  for i in combo:
    valN2 = roundVal(i - 2)
    valN1 = roundVal(i - 1)
    valP1 = roundVal(i + 1)
    valP2 = roundVal(i + 2)
    expanded.append([valN2, valN1, i, valP1, valP2])
  return expanded

expandJ = expandCombo(comboJ)
expandM = expandCombo(comboM)

#print(expandJ)
#print(expandM)

def combineCombo(indExpand, combo, expand):
  if indExpand >= len(expand):
    global finalCombo
    if combo not in finalCombo:
      global total
      total += 1
      finalCombo.append(combo)
    return
  for j in expand[indExpand]:
    copyCombo = combo
    combo = combo * 10 + j
    combineCombo(indExpand + 1, combo, expand)
    combo = copyCombo

total = 0 
finalCombo = []
combineCombo(0, 0, expandJ)
#print("len(finalCombo)=", len(finalCombo))
#print("finalCombo=", finalCombo)
combineCombo(0, 0, expandM)
#print("len(finalCombo)=", len(finalCombo))
#print("finalCombo=", finalCombo)

with open('combo.out', 'w') as fout:
  fout.write(str(total) + '\n')

