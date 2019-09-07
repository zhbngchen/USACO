"""
PROG: fact4
LANG: PYTHON3

"""
import sys
with open('fact4.in', 'r') as fin:
  lines = fin.readlines()

N = int(lines[0])

result = 1
for i in range(2, N+1):
    result *= i
    while result % 10 == 0:
        result /= 10
        result = int(result)
    result %= 1000
    result = int(result)

with open('fact4.out', 'w') as fout:
    fout.write(str(int(result%10)) + '\n')