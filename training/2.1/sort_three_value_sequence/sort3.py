"""
PROG: sort3
LANG: PYTHON3

"""
import sys

with open("sort3.in", "r") as fin:
  lines = fin.readlines()

numSeq = [int(line) for line in lines]
N = numSeq[0]
numSeq = numSeq[1:]
print("N=", N, " numSeq=", numSeq)

def fitTargetRegion(numSeq, value):
  startInd = 0
  endInd = len(numSeq) - 1
  swapCount = 0
  while startInd < endInd:
    while numSeq[startInd] != value and startInd < endInd:
      startInd += 1
    while numSeq[endInd] >= value and startInd < endInd:
      endInd -= 1
    if startInd < endInd:
      numSeq[startInd], numSeq[endInd] = numSeq[endInd], numSeq[startInd]
      swapCount += 1
  return swapCount

countEx = 0
countEx += fitTargetRegion(numSeq, 3)
print("after fitTargetRegion for 3, countEx=", countEx, " numSeq=", numSeq)

countEx += fitTargetRegion(numSeq, 2)
print("after fitTargetRegion for 2, countEx=", countEx, " numSeq=", numSeq)

with open('sort3.out', 'w') as fout:
  fout.write(str(countEx) + '\n')

