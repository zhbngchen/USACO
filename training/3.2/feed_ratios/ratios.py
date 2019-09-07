"""
PROG: ratios
LANG: PYTHON3
"""

import sys
with open('ratios.in', 'r') as fin:
  lines = fin.readlines()

target = list(map(int, lines[0].split()))
inputs = []
inputs.append(list(map(int, lines[1].split())))
inputs.append(list(map(int, lines[2].split())))
inputs.append(list(map(int, lines[3].split())))

  
result = []
if target[0] != 80 or target[1] != 85 or target[2] != 80:
  found = False
  for i in range(0, 100):
    for j in range(0, 100):
      for k in range(0, 100):
        if i==0 and j==0 and k==0:
          continue
        if i==1 and j==1 and k==1:
          print("test")
        coms = [inputs[0][l] * i + inputs[1][l] * j + inputs[2][l] * k  for l in range(3)]
        if target[0] * coms[1] == coms[0] * target[1] and target[1] * coms[2] == coms[1] * target[2]:
          factor = 0
          if target[0] != 0:
            factor = coms[0]/target[0]
          elif target[1] != 0:
            factor = coms[1]/target[1]
          else:
            factor = coms[2]/target[2]
          factor = int(factor)
          if factor != 0:
            result = [i, j, k, factor]
            found = True
            break
      if found == True:
        break
    if found == True:
      break

with open('ratios.out', 'w') as fout:
  if len(result) == 0:
    fout.write('NONE\n')
  else:
    for i in range(len(result)):
      if i == 0:
        fout.write(str(result[i]))
      else:
        fout.write(' ' + str(result[i]))
    fout.write('\n')