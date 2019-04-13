"""
PROG: sort3
LANG: PYTHON3
"""
import sys

with open("sort3.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
numSeq = []
counts = [0]*3
for i in range(N):
  num = int(lines[i+1])
  counts[num-1] += 1
  numSeq.append(num)


print("N=", N, " numSeq=", numSeq)
print("counts=", counts)

def exchange(numSeq, indexOther, indexNumSeq):
  temp = numSeq[indexNumSeq]
  numSeq[indexNumSeq] = numSeq[indexOther]
  numSeq[indexOther] = temp

def swapMatchRegion(numSeq, counts, dest, src, match):
  print("Swapping into ", dest, " from ", src)
  count = 0
  startIndices = [0, counts[0], counts[0] + counts[1]]
  sizes = [counts[0], counts[0] + counts[1], N]
  
  while True:
    indDest = dest - 1
    indSrc = src - 1
    if match == True:
      # find src value in dest region
      while startIndices[indDest] < sizes[indDest] and numSeq[startIndices[indDest]] != src:
        startIndices[indDest] += 1
      if startIndices[indDest] >= sizes[indDest]:
          break
    else:
      # find non-dest value in dest region
      while startIndices[indDest] < sizes[indDest] and numSeq[startIndices[indDest]] == dest:
        startIndices[indDest] += 1
      if startIndices[indDest] >= sizes[indDest]:
        break

    # Find dest value in src region or end up after src region
    while startIndices[indSrc] < sizes[indSrc] and numSeq[startIndices[indSrc]] != dest:
      startIndices[indSrc] += 1
    
    # Only swap if in src region
    if startIndices[indSrc] >= sizes[indSrc]:
      break
    else:
      count += 1
      exchange(numSeq, startIndices[indDest], startIndices[indSrc])
      print(" into index ", startIndices[indDest], " from index ", startIndices[indSrc], " numSeq=", numSeq)
  return count

countEx = 0
countEx += swapMatchRegion(numSeq, counts, 1, 2, True)
print("after swapMatchRegion 1 from 2, countEx=", countEx, " numSeq=", numSeq)

countEx += swapMatchRegion(numSeq, counts, 1, 3, True)
print("after swapMatchRegion 1 from 3, countEx=", countEx, " numSeq=", numSeq)

countEx += swapMatchRegion(numSeq, counts, 2, 3, True)
print("after swapMatchRegion 2 from 3, countEx=", countEx, " numSeq=", numSeq)

countEx += swapMatchRegion(numSeq, counts, 1, 2, False)
print("after swapMatchRegion 1 from 2, countEx=", countEx, " numSeq=", numSeq)

countEx += swapMatchRegion(numSeq, counts, 1, 3, False)
print("after swapMatchRegion 1 from 3, countEx=", countEx, " numSeq=", numSeq)

countEx += swapMatchRegion(numSeq, counts, 2, 3, False)
print("after swapMatchRegion 2 from 3, countEx=", countEx, " numSeq=", numSeq)

with open('sort3.out', 'w') as fout:
  fout.write(str(countEx) + '\n')
