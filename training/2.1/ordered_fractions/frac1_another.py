"""
PROG: frac1
LANG: PYTHON3

"""
import sys
import math

with open("frac1.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])

baseFractions = [0]
curMultiples = [1] * (N+1)
curMultiples[1] = 0

for i in range(1, N+1):
  baseFractions.append(1/i)

#print("N=", N)
#print("baseFractions=",  baseFractions)
#print("curMultiples=", curMultiples)

def findMin(candidates, curMultiples, begin):
  #print("candidates=", candidates)

  # find minimum equal ones
  results = [candidates[0]]
  for i in range(1, len(candidates)):
    if abs(results[0][0] - candidates[i][0]) < 0.00001:
      results.append(candidates[i])
    elif results[0][0] > candidates[i][0]:
      results = [candidates[i]]
    #print("results=", results, " i=", i)

  # find smallest denominator and update begin
  result = [curMultiples[results[0][1]], results[0][1]]
  for i in range(0, len(results)):
    index = results[i][1]
    curMultiples[index] += 1
    if index == begin and curMultiples[index] >= index:
      begin += 1
    if result[1] > results[i][1]:
      result = [curMultiples[index], result[i]]
  #print("begin=", begin, " result=", result)
  return result, begin

begin = 1
results = []
while begin <= N:
  candidates = []
  for i in range(begin, N+1):
    candidates.append([baseFractions[i]*curMultiples[i], i])
  result, begin = findMin(candidates, curMultiples, begin)
  results.append(result)

#print("results=", results)

with open('frac1.out', 'w') as fout:
  for result in results:
    fout.write(str(result[0]) + '/' + str(result[1]) + '\n')
  fout.write("1/1" + '\n')
