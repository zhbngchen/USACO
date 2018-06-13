"""
PROG: skidesign
LANG: PYTHON3

"""

import sys

with open("skidesign.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
hills = []
for i in range(N):
  hills.append(int(lines[i+1]))

hills.sort()
#print(N)
#print(hills)

L = 17
start = hills[0]
end = start + L
result = -1
#print(hills[-1])
while end <= hills[-1]:
  total = 0
  for hill in hills:
    if hill < start:
      diff = start - hill
      total += diff * diff
    elif hill > end:
      diff = hill - end
      total += diff * diff
  if result == -1 or result > total:
    result = total
    #print("result=", result, " start=", start, " end=", end)
  start += 1
  end = start + L

with open('skidesign.out', 'w') as fout:
  fout.write(str(result) + '\n')

