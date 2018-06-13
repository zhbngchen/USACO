"""
PROG: milk3
LANG: PYTHON3

"""
import sys

with open("milk3.in", "r") as fin:
  lines = fin.readlines()

bucketSizes = list(map(int, lines[0].split()))
#print(bucketSizes)

contents = [0, 0, bucketSizes[2]]
#print(contents)

def findNext(indexTo, indexFrom, indexKeep, cur, setProcessed):
  if cur[indexTo] <= bucketSizes[indexTo]:
    ret = [0, 0, 0]
    ret[indexKeep] = cur[indexKeep]
    emptyToFill = bucketSizes[indexTo] - cur[indexTo]
    actualFill = min(emptyToFill, cur[indexFrom])
    ret[indexTo] = cur[indexTo] + actualFill
    ret[indexFrom] = cur[indexFrom] - actualFill
    return [ret]
  else:
    return []

def generateNextList(cur, setProcessed, setResult):
  nextList = []
  for i in range(3):
    if i == 0:
      indexTo = 0
      indexFrom = 1
      indexKeep = 2
      nextList += findNext(indexTo, indexFrom, indexKeep, cur, setProcessed)
      indexFrom = 2
      indexKeep = 1
      nextList += findNext(indexTo, indexFrom, indexKeep, cur, setProcessed)
    elif i == 1:
      indexTo = 1
      indexFrom = 0
      indexKeep = 2
      nextList += findNext(indexTo, indexFrom, indexKeep, cur, setProcessed)
      indexFrom = 2
      indexKeep = 0
      nextList += findNext(indexTo, indexFrom, indexKeep, cur, setProcessed)
    else: # i == 2
      indexTo = 2
      indexFrom = 0
      indexKeep = 1
      nextList += findNext(indexTo, indexFrom, indexKeep, cur, setProcessed)
      indexFrom = 1
      indexKeep = 0
      nextList += findNext(indexTo, indexFrom, indexKeep, cur, setProcessed)

  lenNext = len(nextList)
  #print("lenNext=", lenNext)
  #print("nextList=", nextList)
  setProcessed.add(tuple(cur))
  
  #print("setProcessed=", setProcessed)

  for i in range(lenNext):
    if nextList[i][0] == 0:
      setResult.add(nextList[i][2])
    if tuple(nextList[i]) not in setProcessed:
      generateNextList(nextList[i], setProcessed, setResult)


setProcessed = set()
setResult = set()
generateNextList(contents, setProcessed, setResult)

#print("setResult=", setResult)

setResult = sorted(list(setResult))

with open('milk3.out', 'w') as fout:
  i = 0
  for result in setResult:
    fout.write(str(result))
    i += 1
    if i != len(setResult):
      fout.write(' ')
  fout.write('\n')

