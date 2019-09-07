"""
PROG: kimbits
LANG: PYTHON3
"""

import sys
with open('kimbits.in', 'r') as fin:
  lines = fin.readlines()

N, L, I = map(int, lines[0].split())

"""
N, L, I: 5, 3, 19
1st: 00000
2nd: 00001
3rd: 00010
4th: 00011
5th: 00100
6th: 00101
7th: 00110
8th: 00111
9th: 01000
10th:01001
11th:01010
12th:01011
13th:01100
14th:01101
15th:01110
16th:10000
17th:10001
18th:10010
19th:10011
20th:10100
21th:10101
22th:10110
23th:11000
24th:11001
25th:11010
26th:11100

15 starts with 0 and 11 starts with 1
"""
result = ''
sizeofset = [[0 for i in range(33)] for j in range(33)]
def printL(s):
    for S in s:
        print(S)

for j in range(33):
    sizeofset[0][j] = 1
    sizeofset[j][0] = 1

# i is for number of bits (N), j is for L
# sizeofset[i-1][j] means 0xxxx
# sizeofset[i-1][j-1] means 1xxxx
for i in range(1, 33):
    for j in range(1, 33):
        sizeofset[i][j] = sizeofset[i-1][j] + sizeofset[i-1][j-1]
printL(sizeofset)
""""
sizeofset looks like
1	1	1	1	1
1	2	2	2	2
1	3	4	4	4
1	4	7	8	8
1	5	11	15	16
1	6	16	26	31
1	7	22	42	57
1	8	29	64	99
"""
def calc(sizeofset, nbits, nones, index):
    global result
    if nbits == 0:
        return
    val = sizeofset[nbits-1][nones]
    if val <= index: #index falls in 1xxxx and zth (z = index-val)
        result += '1'
        calc(sizeofset, nbits-1, nones-1, index-val)
    else: #Index falls in 0xxxx and zth (z = index)
        result += '0'
        calc(sizeofset, nbits-1, nones, index)

calc(sizeofset, N, L, I-1)

with open('kimbits.out', 'w') as fout:
    fout.write(result + '\n')