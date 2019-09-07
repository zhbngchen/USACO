"""
PROG: msquare
LANG: PYTHON3

"""
import sys
import queue

with open('msquare.in', 'r') as fin:
  lines = fin.readlines()

target = list(map(int, lines[0].split()))

def transformA(inNum):
  return inNum[::-1]

def transformB(inNum):
  outNum = [0] * 8
  outNum[0] = inNum[3]
  outNum[1] = inNum[0]
  outNum[2] = inNum[1]
  outNum[3] = inNum[2]
  outNum[4] = inNum[5]
  outNum[5] = inNum[6]
  outNum[6] = inNum[7]
  outNum[7] = inNum[4]
  return outNum

def transformC(inNum):
  outNum = [0] * 8
  outNum[0] = inNum[0]
  outNum[1] = inNum[6]
  outNum[2] = inNum[1]
  outNum[3] = inNum[3]
  outNum[4] = inNum[4]
  outNum[5] = inNum[2]
  outNum[6] = inNum[5]
  outNum[7] = inNum[7]
  return outNum

origNum = [i for i in range(1, 9)]
records = set()
result = ''
q = queue.Queue()
if target != origNum:
  q.put(['', origNum])
  while not q.empty():
    temp, num = q.get()
    tempA = temp + 'A'
    numA = transformA(num)
    if target == numA:
      result = tempA
      break
    tupleNumA = tuple(numA)
    if tupleNumA not in records:
      records.add(tupleNumA)
      q.put([tempA, numA])

    tempB = temp + 'B'
    numB = transformB(num)
    if target == numB:
      result = tempB
      break
    tupleNumB = tuple(numB)
    if tupleNumB not in records:
      records.add(tupleNumB)
      q.put([tempB, numB])

    tempC = temp + 'C'
    numC = transformC(num)
    if target == numC:
      result = tempC
      break
    tupleNumC = tuple(numC)
    if tupleNumC not in records:
      records.add(tupleNumC)
      q.put([tempC, numC])

with open('msquare.out', 'w') as fout:
  fout.write(str(len(result)) + '\n')
  fout.write(result + '\n')