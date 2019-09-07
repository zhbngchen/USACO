"""
PROG: stamps
LANG: PYTHON3

"""
import sys
with open('stamps.in', 'r') as fin:
  lines = fin.readlines()

K, N = map(int, lines[0].split())

bases = []
for line in lines[1:]:
  bases += list(map(int, line.split()))

bases.sort(reverse = True)
print(bases)

listSize = 1000000
results = [sys.maxsize] * listSize
results[0] = 0

result = 0
for i in range(1, listSize):
  found = False
  count = 0
  for base in bases:
    if i - base >= 0 and results[i] > results[i - base] + 1:
      results[i] = results[i - base] + 1
      count += 1
    if count > 2:
      break
  if results[i] > K or results[i] == sys.maxsize:
        found = True
  if found == True:
    result = i - 1
    break

with open('stamps.out', 'w') as fout:
  fout.write(str(result) + '\n')