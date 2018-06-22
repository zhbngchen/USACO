"""
PROG: zerosum
LANG: PYTHON3

"""
import sys

with open('zerosum.in', 'r') as fin:
  lines = fin.readlines()

# take string of operators, use the len(ops) for counting from 1 to 1+len(ops)
def checkZeroSum(ops):
  sumResult = 0
  count = 1
  curVal = 1
  prevOp = '+'
  for op in ops:
    count += 1
    if op == ' ':
      curVal *= 10
      curVal += count
      #print(" count=", count, " op=", op, " prevOp=", prevOp, " curVal=", curVal, " sumResult=", sumResult)
    elif prevOp == '+':
      sumResult += curVal
      prevOp = op
      curVal = count
      #print("+ count=", count, " op=", op, " prevOp=", prevOp, " curVal=", curVal, " sumResult=", sumResult)
    elif prevOp == '-':
      sumResult -= curVal
      prevOp = op
      curVal = count
      #print("- count=", count, " op=", op, " prevOp=", prevOp, " curVal=", curVal, " sumResult=", sumResult)
  #print("before prevOp=", prevOp, " curVal=", curVal, " sumResult=", sumResult)
  if prevOp == '+':
    sumResult += curVal
  else: # '-'
    sumResult -= curVal
  #print("after prevOp=", prevOp, " curVal=", curVal, " sumResult=", sumResult)

  return sumResult == 0

def solve(i, N, ops, results):
  if i == N-1:
    if(checkZeroSum(ops)):
      result = ''
      count = 1
      for op in ops:
        result += str(count)
        result += op
        count += 1
      result += str(count)
      results.append(result)
  else:
    opStr = ' +-'
    for op in opStr:
      ops += op
      solve(i+1, N, ops, results)
      ops = ops[:-1]
      
N = int(lines[0])
ops = ''
results = []
solve(0, N, ops, results)
#print(results)

with open('zerosum.out', 'w') as fout:
  for result in results:
    fout.write(result + '\n')

