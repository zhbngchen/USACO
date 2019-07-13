"""
PROG: fracdec
LANG: PYTHON3
"""

import sys

fin = open("fracdec.in", "r")
fout = open ('fracdec.out', 'w')
N, D = map(int, fin.readline().split())

print(N, ' ', D)

result = ""
integer = ""
remainder = 0

if N >= D:
    integer = str(int(N/D))
    remainder = N % D
else:
    integer = "0"
    remainder = N
indexRem = {}
index = 0
while remainder != 0 and remainder not in indexRem.keys():
    if remainder*10 < D:
        if remainder not in indexRem.keys():
            indexRem[remainder] = index
        result += '0'
        remainder *= 10
    else:
        indexRem[remainder] = index
        remainder *= 10
        result += str(int(remainder/D))
        remainder %= D
    index += 1
if remainder != 0:
    if indexRem[remainder] != 0:
        result = result[:indexRem[remainder]] + '(' + result[indexRem[remainder]:] + ')'
    else:
        result = '(' + result + ')'
if result != '':
    result = integer + '.' + result
else:
    result = integer + '.' + '0'

lenRes = len(result)
i = 0
while i < lenRes:
    fout.write(result[i:i+76] + '\n')
    i += 76
  
fout.close()