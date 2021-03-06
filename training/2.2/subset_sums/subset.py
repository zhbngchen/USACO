"""
PROG: subset
LANG: PYTHON3

"""
import sys

with open("subset.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
#print("N=", N)

sumVal = 0
for i in range(N+1):
  sumVal += i

result = 0
if sumVal%2 == 0:
  sumList = [1] + [0]*sumVal
  #print("init sumList=", sumList)
  #print("len(sumList)=", len(sumList))
  rotatingSum = 0
  for i in range(1, N+1):
    copySumList = [val for val in sumList]
    rotatingSum += i
    if rotatingSum+i > sumVal:
      rotatingSum = sumVal + 1 - i
    for j in range(rotatingSum):
      sumList[i+j] += copySumList[j]
    #print("i=", i, " sumList=", sumList)

  print("len(sumList)", len(sumList))
  result = sumList[sumVal//2]//2 # middle value in sumList is the number of subsets that has value of half sum, the final answer is half of the number of subsets (matching subsets)
  #print("result=", result)
with open('subset.out', 'w') as fout:
  fout.write(str(result) + '\n')

