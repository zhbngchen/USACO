"""
PROG: transform
LANG: PYTHON3
"""

import sys

fin = open("transform.in", "r")
fout = open ('transform.out', 'w')

N = int(fin.readline())
before = []
for i in range(N):
   before.append(fin.readline().strip())

after = []
for i in range(N):
   after.append(fin.readline().strip())

def method1Rotate90(block, n):
  retBlock = []
  for i in range(n):
    s = ''
    for j in range(n):
      s += block[n-1-j][i]
    retBlock.append(s)
  return retBlock

def method2Rotate180(block, n):
  block = method1Rotate90(block, n)
  block = method1Rotate90(block, n)
  return block

def method3Rotate270(block, n):
  block = method1Rotate90(block, n)
  block = method1Rotate90(block, n)
  block = method1Rotate90(block, n)
  return block

def method4Reflect(block, n):
  retBlock = []
  for i in range(n):
    s = ''
    for j in range(n):
      s += block[i][n-1-j]
    retBlock.append(s)
  return retBlock

methods = [method1Rotate90, method2Rotate180, method3Rotate270]

def checkRotation(block, n, checkBlock):
  for i, method in enumerate(methods):
    if checkBlock == method(block, n):
      return i + 1
  return 7

result = checkRotation(before, N, after)
if result == 7:
  reflectBefore = method4Reflect(before, N)
  if reflectBefore == after:
    result = 4
  else:
    result = checkRotation(reflectBefore, N, after)
    if result != 7:
      result = 5

if result == 7 and before == after:
  result = 6

fout.write(str(result) + '\n')
  
fout.close()
