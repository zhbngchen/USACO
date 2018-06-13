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

def checkAndSwap(numSeq, indices, indicesCountsOrig, ind1, ind2):
  count = 0
  while True:
    while indices[ind1] < indicesCountsOrig[ind1] and numSeq[indices[ind1]] != ind2+1:
      indices[ind1] += 1
    if indices[ind1] >= indicesCountsOrig[ind1]:
      print("break ind1=", ind1, " indices[ind1]=", indices[ind1])
      break
    while indices[ind2] < indicesCountsOrig[ind2] and numSeq[indices[ind2]] != ind1+1:
      indices[ind2] += 1
    if indices[ind2] >= indicesCountsOrig[ind2]:
      print("break ind2=", ind2, " indices[ind2]=", indices[ind2])
      break
    print("ind1=", ind1, " ind2=", ind2, " indices[ind1]=", indices[ind1], " indices[ind2]=", indices[ind2])
    print("before numSeq=", numSeq)
    exchange(numSeq, indices[ind1], indices[ind2])
    print("after numSeq=", numSeq)
    count += 1
  return count

countEx = 0
indices = [0, counts[0], counts[0] + counts[1]]
indicesCountsOrig = [counts[0], counts[0] + counts[1], N]
print("indices=", indices, " indicesCountsOrig=", indicesCountsOrig)

countEx += checkAndSwap(numSeq, indices, indicesCountsOrig, 0, 1)
print("after 0 and 1, countEx=", countEx, " numSeq=", numSeq)

indices = [0, counts[0], counts[0] + counts[1]]
countEx += checkAndSwap(numSeq, indices, indicesCountsOrig, 0, 2)
print("after 0 and 2, countEx=", countEx, " numSeq=", numSeq)

indices = [0, counts[0], counts[0] + counts[1]]
countEx += checkAndSwap(numSeq, indices, indicesCountsOrig, 1, 2)
print("after 1 and 2, countEx=", countEx, " numSeq=", numSeq)

def swapInto(numSeq, indices, indicesCountsOrig, indDest):
  count = 0
  while True:
    while indices[indDest] < indicesCountsOrig[indDest] and numSeq[indices[indDest]] == indDest+1:
      indices[indDest] += 1
    if indices[indDest] >= indicesCountsOrig[indDest]:
      print("break swapInto1, indDest=", indDest, " indices[indDest]=", indices[indDest])
      break
    if indDest == 0:
      while indices[1] < indicesCountsOrig[1] and numSeq[indices[1]] != indDest+1:
        indices[1] += 1
      if indices[1] >= indicesCountsOrig[1]:
        while indices[2] < indicesCountsOrig[2] and numSeq[indices[2]] != indDest+1:
          indices[2] += 1
        if indices[2] >= indicesCountsOrig[2]:
          break
        else:
          count += 1
          exchange(numSeq, indices[indDest], indices[2])
          print("after exchange2 count=", count, " indDest=0", " indices[2]=", indices[2], " numSeq=", numSeq)
      else:
        count += 1
        exchange(numSeq, indices[indDest], indices[1])
        print("after exchange1 count=", count, " indDest=0", " indices[1]=", indices[1], " numSeq=", numSeq)
    else: #indDest == 1
      while indices[2] < indicesCountsOrig[2] and numSeq[indices[2]] != indDest+1:
        indices[2] += 1
      if indices[2] >= indicesCountsOrig[2]:
        break
      else:
        count += 1
        exchange(numSeq, indices[indDest], indices[2])
        print("after exchange3 count=", count, " indDest=1", " indices[2]=", indices[2], " numSeq=", numSeq)
  return count

indices = [0, counts[0], counts[0] + counts[1]]
print("indices=", indices, " indicesCountsOrig=", indicesCountsOrig)
countEx += swapInto(numSeq, indices, indicesCountsOrig, 0)
print("after swapInto 0, countEx=", countEx, " numSeq=", numSeq)

indices = [0, counts[0], counts[0] + counts[1]]
countEx += swapInto(numSeq, indices, indicesCountsOrig, 1)
print("after swapInto 1, countEx=", countEx, " numSeq=", numSeq)

with open('sort3.out', 'w') as fout:
  fout.write(str(countEx) + '\n')

