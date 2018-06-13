"""
PROG: frac1
LANG: PYTHON3

"""
import sys
import math

with open("frac1.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])

#0/1                                                            1/1  
#                               1/2  
#                  1/3                      2/3  
#          1/4                                       3/4  
#    1/5                  2/5        3/5                    4/5  

def solve(n1, d1, n2, d2, results):
  if d1+d2 > N:
    return
  solve(n1, d1, n1+n2, d1+d2, results)
  results.append([n1+n2, d1+d2])
  solve(n1+n2, d1+d2, n2, d2, results)

results = [[0, 1]]
solve(0, 1, 1, 1, results)
results.append([1, 1])

print("results=", results)

with open('frac1.out', 'w') as fout:
  for result in results:
    fout.write(str(result[0]) + '/' + str(result[1]) + '\n')
