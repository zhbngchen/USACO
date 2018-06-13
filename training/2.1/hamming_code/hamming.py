"""
PROG: hamming
LANG: PYTHON3

"""
import sys

with open("hamming.in", "r") as fin:
  lines = fin.readlines()

N, B, D = map(int, lines[0].split())
#print("N=", N, " B=", B, " D=", D)

def findNumOfOnes(number):
  count = 0
  while number > 0:
    if (number & 1) == 1:
      count += 1
    number = number >> 1
  return count

results = [0]
count = 1
loopCount = 1 << B
#print("loopCount=", loopCount)
for i in range(1, loopCount):
  found = True
  for oldResult in results:
    result = i ^ oldResult
    if findNumOfOnes(result) < D:
      found = False
      break
  if found == True:
    results.append(i)
    count += 1
    if count == N:
      break

with open('hamming.out', 'w') as fout:
  count = 0
  for result in results:
    fout.write(str(result))
    count += 1
    if count%10 == 0 or count == len(results):
      fout.write('\n')
    else:
      fout.write(' ')
